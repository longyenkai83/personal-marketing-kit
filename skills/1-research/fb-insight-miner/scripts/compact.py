"""
compact.py — Convert filtered JSON to compact line-based text for Claude reading.

Usage:
    python compact.py <filtered_json> <output_txt>

Reduces token usage ~70% vs raw JSON. Groups comments by post, sorts by likes DESC.
Format per line: [likes|replies|depth|signals] author — text

Requires: PYTHONIOENCODING=utf-8 on Windows.
"""
import json
import sys

def short_id(url):
    if 'reel/' in url:
        return 'R' + url.split('reel/')[1].strip('/')[-6:]
    if 'pfbid' in url:
        return 'P' + url.split('pfbid')[1][:6]
    return url[-10:]

def main(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(out_path, 'w', encoding='utf-8') as f:
        m = data.get('metadata', {})
        f.write(f"# Filtered Comments\n")
        f.write(f"# page_owner: {m.get('page_owner','?')}\n")
        f.write(f"# raw: {m.get('raw_count','?')} | noise: {m.get('filtered_noise','?')} | analyzed: {m.get('total_analyzed','?')}\n")
        f.write(f"# Format: [likes|replies|depth|signals] author — text\n")
        f.write(f"# Signals: TP=top_post LG=long DT=deep_thread HL=high_liked Q=question\n\n")

        by_post = {}
        for c in data.get('comments', []):
            by_post.setdefault(c['post_url'], []).append(c)

        for post_url, comments in by_post.items():
            pid = short_id(post_url)
            comments.sort(key=lambda x: int(x.get('likes', 0) or 0), reverse=True)
            f.write(f"\n=== POST {pid} ({len(comments)} comments) — {post_url}\n")
            for c in comments:
                likes = c.get('likes', 0) or 0
                replies = c.get('replies', 0) or 0
                depth = c.get('depth', 0) or 0
                sig_map = {'top_post':'TP','long':'LG','deep_thread':'DT',
                           'high_liked':'HL','question':'Q'}
                sigs = ''.join(sig_map.get(s,'') for s in c.get('signals',[]))
                text = (c.get('text','') or '').replace('\n', ' ').strip()
                author = (c.get('author','') or 'Anon')[:20]
                f.write(f"[{likes}|{replies}|{depth}|{sigs}] {author} — {text}\n")

    import os
    print(f"Saved: {out_path}")
    print(f"Size: {os.path.getsize(out_path)} bytes")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python compact.py <filtered_json> <output_txt>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])