"""
enrich.py — Phase 4: 6 micro-reports that mine deeper insight from raw comments
without re-scraping. Feed OUTPUT into Claude for narrative synthesis.

Usage:
    python enrich.py <raw_json> <page_owner> <output_txt>

6 micro-reports:
  1. Admin voice decoding (page owner's own replies)
  2. Top commenters — DM outreach lead list
  3. Deep thread conversations (depth ≥2)
  4. N-gram analysis — repeat phrases / VoC
  5. Tag-a-friend mechanic detection
  6. Emoji-emotion fingerprint per post

Requires: PYTHONIOENCODING=utf-8 on Windows.
"""
import json
import re
import sys
from collections import Counter, defaultdict

EMOJI_MAP = {
    'pain_raw': '😭😢😔😞😫😩🥲',
    'pain_cope': '😂🤣😆😅',
    'love': '❤️🥰😍💕💞',
    'gratitude': '🙏🌹🌷',
    'resignation': '😌😔🥱',
    'excited': '🔥✨🥳🎉',
    'thinking': '🤔😶🤨',
    'laugh_sheepish': '😅😬😳',
}

# Vietnamese stopwords for n-gram filtering
STOPWORDS = {'là','có','không','được','và','của','với','đã','này','đó','nhé','vậy','mà','thì','cho','để','ơi','ạ','em','chị','my','bạn','mình','anh','tôi','nó','rồi','cũng','lại','đi','trong','cảm','ơn','rất','hay','quá','nè','nhé','nha','ạ','ơi','thôi','nữa','một','hai','người','cái','khi','thật','tự','sẽ','còn','những','vào','như','gì','ra','từ','bị','vì','hơn','nếu','dạ','lúc','nên','về','luôn','mới','hết','giờ','ai','hay','nói'}

def short(url):
    if 'reel/' in url: return 'R' + url.split('reel/')[1].strip('/')[-6:]
    if 'pfbid' in url: return 'P' + url.split('pfbid')[1][:6]
    return url[-10:]

def words(t): return len((t or '').strip().split())

def tokenize(t):
    t = re.sub(r'[^\w\sàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]', ' ', (t or '').lower())
    return [tok for tok in t.split() if len(tok) > 1]

def looks_like_tag(text):
    if not text: return False
    words_ = text.strip().split()
    if len(words_) < 2: return False
    first = words_[:3]
    caps = sum(1 for w in first if w and w[0].isupper())
    return caps >= 2 and any(len(w) >= 2 for w in first)

def main(raw_path, page_owner, out_path):
    with open(raw_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    items = data.get('items', data) if isinstance(data, dict) else data

    lines = []
    def w(s=''): lines.append(str(s))

    w("="*70)
    w(f"📊 ENRICHMENT REPORT — {page_owner} (mining {len(items)} raw comments)")
    w("="*70)

    # ============ 1. ADMIN VOICE ============
    w("\n\n" + "="*70)
    w(f"1️⃣  ADMIN VOICE DECODING — {page_owner}'s replies")
    w("="*70)
    admin = [c for c in items if c.get('profileName') == page_owner]
    w(f"\nAdmin replies: {len(admin)}")
    if admin:
        w(f"Avg length: {sum(words(c.get('text','')) for c in admin)/len(admin):.1f} words")
        w(f"Reply rate: {len(admin)*100//len(items)}% of all comments")
        admin_by_post = defaultdict(list)
        for c in admin: admin_by_post[c.get('inputUrl','')].append(c)
        total_posts = len(set(c.get('inputUrl','') for c in items))
        w(f"Posts admin replied on: {len(admin_by_post)} / {total_posts}")
        short_r = [c for c in admin if words(c.get('text','')) < 8]
        long_r = [c for c in admin if words(c.get('text','')) > 20]
        link_r = [c for c in admin if '.com' in (c.get('text','') or '')]
        w(f"\n- Short replies (<8 words): {len(short_r)}")
        w(f"- Long replies (>20 words): {len(long_r)} (teaching mode)")
        w(f"- Link replies: {len(link_r)} (funnel push)")

        w("\n### Top 5 LONGEST admin replies (teaching voice):")
        for c in sorted(long_r, key=lambda x: words(x.get('text','')), reverse=True)[:5]:
            txt = (c.get('text','') or '').replace('\n',' ')[:400]
            w(f"\n  [{c.get('likesCount',0)} likes] on {short(c.get('inputUrl',''))}")
            w(f"  \"{txt}\"")

    # ============ 2. TOP COMMENTERS ============
    w("\n\n" + "="*70)
    w("2️⃣  TOP COMMENTERS — DM outreach lead list")
    w("="*70)
    profile_stats = defaultdict(lambda: {'count':0,'total_likes':0,'comments':[],'name':''})
    for c in items:
        if c.get('profileName') == page_owner: continue
        pid = c.get('profileId','')
        if not pid: continue
        profile_stats[pid]['count'] += 1
        try: profile_stats[pid]['total_likes'] += int(c.get('likesCount',0) or 0)
        except ValueError: pass
        profile_stats[pid]['comments'].append(c)
        profile_stats[pid]['name'] = c.get('profileName','')

    repeat = sorted([(pid,s) for pid,s in profile_stats.items() if s['count']>=3],
                     key=lambda x:(x[1]['count'], x[1]['total_likes']), reverse=True)
    w(f"\nRepeat engagers (≥3 posts): {len(repeat)} superfans")
    w("\n### Top 15 superfans:")
    for pid, s in repeat[:15]:
        w(f"  [{s['count']} posts, {s['total_likes']} likes] {s['name']}")
        sample = max(s['comments'], key=lambda x: int(x.get('likesCount',0) or 0))
        txt = (sample.get('text','') or '').replace('\n',' ')[:100]
        w(f"    sample: \"{txt}\"")

    one_shot = sorted([(pid,s) for pid,s in profile_stats.items()
                        if s['count']==1 and s['total_likes']>=10],
                       key=lambda x:x[1]['total_likes'], reverse=True)
    w(f"\nOne-shot high-impact (1 comment, ≥10 likes): {len(one_shot)}")
    w("\n### Top 10 one-shot influencers (DM priority):")
    for pid, s in one_shot[:10]:
        c = s['comments'][0]
        txt = (c.get('text','') or '').replace('\n',' ')[:150]
        w(f"  [{s['total_likes']} likes] {s['name']} — \"{txt}\"")

    # ============ 3. DEEP THREADS ============
    w("\n\n" + "="*70)
    w("3️⃣  DEEP THREAD CONVERSATIONS (depth ≥2)")
    w("="*70)
    deep = [c for c in items if c.get('threadingDepth',0)>=2]
    w(f"\nDepth-2+ comments: {len(deep)}")
    deep_by_post = defaultdict(list)
    for c in deep: deep_by_post[c.get('inputUrl','')].append(c)
    w("\n### Posts with most debate depth:")
    for post, cmts in sorted(deep_by_post.items(), key=lambda x:len(x[1]), reverse=True)[:5]:
        w(f"\n  {short(post)} — {len(cmts)} deep replies")
        for c in cmts[:5]:
            author = c.get('profileName','')[:20]
            txt = (c.get('text','') or '').replace('\n',' ')[:130]
            w(f"    [{c.get('likesCount',0)}L d={c.get('threadingDepth')}] {author}: \"{txt}\"")

    # ============ 4. N-GRAM ============
    w("\n\n" + "="*70)
    w("4️⃣  N-GRAM ANALYSIS — repeat phrases / VoC")
    w("="*70)
    user_texts = [(c.get('text','') or '').lower()
                   for c in items
                   if c.get('profileName')!=page_owner and words(c.get('text',''))>=3]
    bigrams = Counter(); trigrams = Counter()
    for t in user_texts:
        toks = tokenize(t)
        for i in range(len(toks)-1): bigrams[(toks[i],toks[i+1])] += 1
        for i in range(len(toks)-2): trigrams[(toks[i],toks[i+1],toks[i+2])] += 1
    def is_boring(g): return all(t in STOPWORDS or len(t)<=2 for t in g)

    w("\n### Top 30 meaningful bigrams:")
    ctr = 0
    for g, n in bigrams.most_common(200):
        if n < 2: break
        if is_boring(g): continue
        w(f"  {n:3d}  \"{' '.join(g)}\"")
        ctr += 1
        if ctr >= 30: break

    w("\n### Top 20 meaningful trigrams:")
    ctr = 0
    for g, n in trigrams.most_common(200):
        if n < 2: break
        if is_boring(g): continue
        w(f"  {n:3d}  \"{' '.join(g)}\"")
        ctr += 1
        if ctr >= 20: break

    # ============ 5. TAG-A-FRIEND ============
    w("\n\n" + "="*70)
    w("5️⃣  TAG-A-FRIEND PATTERN — viral mechanics")
    w("="*70)
    tags = [c for c in items if c.get('profileName')!=page_owner
             and looks_like_tag(c.get('text',''))]
    w(f"\nTag-a-friend comments: {len(tags)} ({len(tags)*100//max(len(items),1)}% of all)")
    tag_by_post = Counter(c.get('inputUrl','') for c in tags)
    w("\n### Posts with most tag activity:")
    for post, n in tag_by_post.most_common(5):
        w(f"  {n:3d} tags  — {short(post)}")
    if tag_by_post:
        top = tag_by_post.most_common(1)[0][0]
        w(f"\n### Sample tags from top post ({short(top)}):")
        for c in [c for c in tags if c.get('inputUrl')==top][:10]:
            txt = (c.get('text','') or '').replace('\n',' ')[:120]
            w(f"  \"{txt}\"")

    # ============ 6. EMOJI-EMOTION ============
    w("\n\n" + "="*70)
    w("6️⃣  EMOJI-EMOTION MAP per post")
    w("="*70)
    emoji_by_post = defaultdict(Counter)
    for c in items:
        if c.get('profileName')==page_owner: continue
        text = c.get('text','') or ''
        for cat, emojis in EMOJI_MAP.items():
            for e in emojis:
                if e in text: emoji_by_post[c.get('inputUrl','')][cat] += 1
    w("\n### Top 10 posts by emotional fingerprint:")
    post_totals = {p: sum(cats.values()) for p, cats in emoji_by_post.items()}
    for post, total in sorted(post_totals.items(), key=lambda x:x[1], reverse=True)[:10]:
        w(f"\n  {short(post)} — {total} emoji signals")
        for cat, n in emoji_by_post[post].most_common():
            w(f"    {cat}: {n}")

    w("\n\n" + "="*70)
    w("END ENRICHMENT REPORT")
    w("="*70)

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    import os
    print(f"Saved: {out_path}")
    print(f"Size: {os.path.getsize(out_path)} bytes / {len(lines)} lines")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python enrich.py <raw_json> <page_owner> <out_txt>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])