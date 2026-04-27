"""
sample.py — Apply strategic sampling rules to raw Apify FB comments output.

Usage:
    python sample.py <raw_json_path> <page_owner_name> <output_json_path> [cap]

Example:
    python sample.py raw-comments.json "Luong Anh My" filtered.json 1500

Requires: PYTHONIOENCODING=utf-8 on Windows to print emoji.
"""
import json
import re
import sys
import random
from collections import Counter

def word_count(text):
    return len((text or '').strip().split())

def is_emoji_only(text):
    if not text:
        return True
    stripped = re.sub(r'[\U0001F300-\U0001FAFF\U00002600-\U000027BF\s\W]', '', text)
    return len(stripped) < 2

def is_tag_only(text):
    stripped = re.sub(r'@\S+|\s+', '', text or '')
    return len(stripped) == 0

def is_promo(text):
    if not text: return False
    t = text.lower()
    return ('luonganhmy.com' in t and ('video được gỡ' in t or 'nhận quà' in t))

def main(raw_path, page_owner, out_path, cap=1500):
    with open(raw_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    items = data.get('items', data) if isinstance(data, dict) else data
    total = len(items)

    print("=" * 60)
    print(f"📊 SAMPLING — page_owner='{page_owner}' | cap={cap}")
    print("=" * 60)
    print(f"Raw comments: {total}")

    filtered_out = {'emoji_only': 0, 'too_short': 0, 'tag_only': 0,
                    'promo': 0, 'duplicate': 0, 'admin_response': 0}
    seen = set()
    high_signal = []

    for c in items:
        text = c.get('text', '') or ''
        if c.get('profileName') == page_owner:
            filtered_out['admin_response'] += 1
            continue
        if is_emoji_only(text):
            filtered_out['emoji_only'] += 1; continue
        if is_tag_only(text):
            filtered_out['tag_only'] += 1; continue
        if word_count(text) < 5:
            filtered_out['too_short'] += 1; continue
        if is_promo(text):
            filtered_out['promo'] += 1; continue
        key = f"{c.get('profileId','')}:{text[:50]}"
        if key in seen:
            filtered_out['duplicate'] += 1; continue
        seen.add(key)
        high_signal.append(c)

    print("\nFiltered out:")
    for k, v in filtered_out.items():
        print(f"  - {k}: {v}")
    filtered_count = sum(filtered_out.values())
    print(f"  TOTAL noise: {filtered_count}")
    print(f"\nAfter Step 1: {len(high_signal)}")

    # Top-5 posts by volume
    post_counts = Counter(c.get('inputUrl','') for c in high_signal)
    top_5 = set([p for p, _ in post_counts.most_common(5)])

    # Tag signals
    for c in high_signal:
        text = c.get('text', '') or ''
        tags = []
        if c.get('inputUrl') in top_5: tags.append('top_post')
        if word_count(text) >= 15: tags.append('long')
        if c.get('threadingDepth', 0) >= 2: tags.append('deep_thread')
        try:
            if int(c.get('likesCount', 0) or 0) >= 10: tags.append('high_liked')
        except ValueError: pass
        if text.rstrip().endswith('?'): tags.append('question')
        c['_signal_tags'] = tags

    must_keep = [c for c in high_signal if c['_signal_tags']]
    unsignaled = [c for c in high_signal if not c['_signal_tags']]
    random.seed(42)
    sampled = random.sample(unsignaled, min(len(unsignaled), max(50, len(unsignaled)//10)))
    final = must_keep + sampled

    if len(final) > cap:
        def priority(c):
            score = 0
            sigs = c['_signal_tags']
            if 'top_post' in sigs: score += 8
            if 'long' in sigs: score += 4
            if 'high_liked' in sigs: score += 4
            if 'deep_thread' in sigs: score += 2
            if 'question' in sigs: score += 2
            try:
                score += min(int(c.get('likesCount',0) or 0) / 10, 5)
            except ValueError: pass
            return -score
        final = sorted(final, key=priority)[:cap]

    print(f"\nHigh-signal kept: {len(must_keep)}")
    print(f"  top_post: {sum('top_post' in c['_signal_tags'] for c in must_keep)}")
    print(f"  long: {sum('long' in c['_signal_tags'] for c in must_keep)}")
    print(f"  deep_thread: {sum('deep_thread' in c['_signal_tags'] for c in must_keep)}")
    print(f"  high_liked: {sum('high_liked' in c['_signal_tags'] for c in must_keep)}")
    print(f"  question: {sum('question' in c['_signal_tags'] for c in must_keep)}")
    print(f"Random sample: {len(sampled)}")
    print("─" * 60)
    print(f"TOTAL ANALYZED: {len(final)} / {total} ({len(final)*100//max(total,1)}%)")

    slim = []
    for c in final:
        slim.append({
            'text': c.get('text', ''),
            'author': c.get('profileName', ''),
            'date': c.get('date', ''),
            'likes': c.get('likesCount', 0),
            'replies': c.get('commentsCount', 0),
            'depth': c.get('threadingDepth', 0),
            'post_url': c.get('inputUrl', ''),
            'signals': c.get('_signal_tags', []),
        })

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump({
            'metadata': {
                'page_owner': page_owner,
                'raw_count': total,
                'filtered_noise': filtered_count,
                'high_signal': len(must_keep),
                'random_sampled': len(sampled),
                'total_analyzed': len(final),
                'top_5_posts': list(top_5),
                'cap': cap,
            },
            'comments': slim,
        }, f, ensure_ascii=False, indent=1)

    print(f"\nSaved: {out_path}")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python sample.py <raw_json> <page_owner_name> <out_json> [cap=1500]")
        sys.exit(1)
    cap = int(sys.argv[4]) if len(sys.argv) > 4 else 1500
    main(sys.argv[1], sys.argv[2], sys.argv[3], cap)