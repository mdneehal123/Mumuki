#!/usr/bin/env python3
"""Builds the product pages, guides, guides hub and genuine-MUMUKI page for www.mumuki.in, and rewrites sitemap.xml.

Run from the repository root:  python3 tools/build_pages.py
Product facts are read from the `products` list in index.html (the single source of truth), so edit products there.
Guide text lives in tools/guides.py. Pages are static HTML; Vercel serves /products/<slug>/ and /guides/<slug>/.
Needs Node.js (to read the products list from index.html).
"""
import html, json, os, re, subprocess, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from guides import GUIDES, GENUINE, REFS  # noqa: E402

SITE = 'https://www.mumuki.in'
WA = '919980881230'
UPDATED = '2026-11-04'
UPDATED_TEXT = '4 November 2026'
esc = html.escape

# ---------- products from index.html ----------
def load_products():
    src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    a = src.index('const products'); b = src.index('];', a) + 2
    js = src[a:b].replace('const products', 'globalThis.products', 1)
    out = subprocess.run(['node', '-e', js + '\nprocess.stdout.write(JSON.stringify(globalThis.products))'], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)

# Page-only details per product id: URL slug, search title, meta description, who it suits, pairs well with, guides.
META = {
    1: dict(slug='honey-banana-pdrn-capsule-ampoule', seo='MUMUKI Honey Banana PDRN Capsule Ampoule (30 ml) India',
            desc='MUMUKI Honey Banana PDRN Capsule Ampoule: banana BDRN, collagen, Manuka honey and ceramide capsules for plumper, glowier skin. Imported from Korea.',
            suits=['Dull or tired-looking skin that needs bounce and glow', 'Dry or dehydrated skin, including in AC rooms', 'Oily skin that wants hydration without stickiness'],
            pairs=[14, 2, 3], guides=['how-to-use-pdrn-serum', 'what-is-pdrn', 'plant-pdrn-vs-salmon-pdrn']),
    2: dict(slug='honey-banana-pdrn-capsule-cream', seo='MUMUKI Honey Banana PDRN Capsule Cream (50 ml) India',
            desc='MUMUKI Honey Banana PDRN Capsule Cream: ceramide capsules, banana BDRN and collagen in a rich, non-greasy moisturiser. Imported from Korea, sold in India.',
            suits=['Dry, tight or flaky skin', 'Sensitive skin (fragrance-free; patch test first)', 'Anyone who wants a moisturiser that works under makeup'],
            pairs=[1, 14, 3], guides=['korean-glass-skin-routine-india', 'is-pdrn-safe', 'pdrn-for-indian-skin']),
    3: dict(slug='honey-banana-pdrn-cream-mist', seo='MUMUKI Honey Banana PDRN Cream Mist India',
            desc='MUMUKI Honey Banana PDRN Cream Mist: a two-layer mist with banana BDRN, milk extract and Manuka honey for hydration on the go. From Korea.',
            suits=['Long days in AC offices', 'Light hydration for most skin types; oily skin may prefer it over sunscreen only', 'Refreshing skin over makeup or sunscreen'],
            pairs=[1, 2, 4], guides=['pdrn-for-indian-skin', 'how-to-use-pdrn-serum', 'pdrn-benefits-for-skin']),
    4: dict(slug='honey-banana-pdrn-ampoule-mask', seo='MUMUKI Honey Banana PDRN Ampoule Sheet Mask (5 Pack) India',
            desc='MUMUKI Honey Banana PDRN Ampoule Mask: 5 sheet masks with banana BDRN, collagen and centella for an instant plump, glowing look. From Korea.',
            suits=['A quick glow before an event, wedding or photoshoot', 'Dry or tired-looking skin', 'A weekly hydration boost'],
            pairs=[2, 13, 1], guides=['how-to-use-korean-face-masks', 'korean-glass-skin-routine-india', 'is-pdrn-safe']),
    13: dict(slug='honey-banana-bdrn-hydrogel-mask', seo='MUMUKI Honey Banana BDRN Overnight Hydrogel Mask (5 Pack)',
             desc='MUMUKI Honey Banana BDRN Hydrogel Mask: 5 overnight hydrogel masks with banana BDRN, collagen and centella that turn clear as they absorb. Sold in India.',
             suits=['Dry or dehydrated skin', 'An overnight hydration treatment', 'Skin that feels tired after travel or late nights'],
             pairs=[4, 2, 1], guides=['how-to-use-korean-face-masks', 'pdrn-benefits-for-skin', 'is-pdrn-safe']),
    14: dict(slug='honey-banana-pdrn-bubble-mask', seo='MUMUKI Honey Banana PDRN Bubble Mask (150 ml) India',
             desc='MUMUKI Honey Banana PDRN Bubble Mask: a leave-on bubble mask with banana BDRN and collagen that melts in within seconds. Step 1 of the 3-step routine.',
             suits=['Rough or uneven-feeling texture', 'Prepping skin before serum', 'A quick daily glow step'],
             pairs=[1, 2, 9], guides=['how-to-use-korean-face-masks', 'korean-glass-skin-routine-india', 'how-to-use-pdrn-serum']),
    9: dict(slug='honey-banana-pdrn-boosting-duo', seo='MUMUKI Honey Banana PDRN Boosting Duo: Bubble Mask + Ampoule',
            desc='MUMUKI Honey Banana PDRN Boosting Duo: the Bubble Mask (150 ml) and Capsule Ampoule (30 ml) together for a two-step glow routine. Sold in India.',
            suits=['Starting a PDRN routine with two steps', 'Dull or dry-feeling skin', 'Gifting'],
            pairs=[2, 10, 3], guides=['how-to-use-pdrn-serum', 'korean-glass-skin-routine-india', 'what-is-pdrn']),
    10: dict(slug='honey-banana-pdrn-3-step-skincare-set', seo='MUMUKI Honey Banana PDRN 3-Step Skincare Set India',
             desc='MUMUKI Honey Banana PDRN 3-Step Skincare Set: Bubble Mask, Capsule Ampoule and Capsule Cream for a complete glass-skin routine. Imported from Korea.',
             suits=['A complete routine in one box', 'Glass-skin glow and hydration', 'Gifting'],
             pairs=[3, 4, 13], guides=['korean-glass-skin-routine-india', 'how-to-use-pdrn-serum', 'pdrn-serum-price-in-india']),
}
ORDER = [1, 2, 3, 4, 13, 14, 9, 10]

def purl(pid): return '/products/%s/' % META[pid]['slug']
def gurl(slug): return '/genuine-mumuki-india/' if slug in ('genuine-mumuki', 'genuine-mumuki-india') else '/guides/%s/' % slug
GBY = {g['slug']: g for g in GUIDES}
def gshort(slug): return GENUINE['short'] if slug in ('genuine-mumuki', 'genuine-mumuki-india') else GBY[slug]['short']
def gblurb(slug):
    g = GENUINE if slug in ('genuine-mumuki', 'genuine-mumuki-india') else GBY[slug]
    return g['dek']
def clean_emoji(t): return re.sub(r'[\U0001F000-\U0001FAFF☀-➿️]\s*', '', t).strip()
def plain(t): return re.sub(r'<[^>]+>', '', t)

WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z"/></svg>'

def wa_link(text): return 'https://wa.me/%s?text=%s' % (WA, urllib.parse.quote(text))

# ---------- shared layout ----------
def head(title, desc, path, image, ld):
    return f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#1E1712">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-96.png" type="image/png" sizes="96x96"><link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MUMUKI India">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE}{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Manrope:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/pages.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<div class="announce">Authentic · imported directly from Korea · Cash on delivery available · Launching soon: join the list for 10% off</div>
<header>
  <div class="wrap nav">
    <button class="menu-toggle" id="menuBtn" aria-label="Menu" aria-expanded="false"><i></i><i></i><i></i></button>
    <nav class="nav-links" id="navLinks">
      <a href="/#shop">Shop</a>
      <a href="/guides/">PDRN guides</a>
      <a href="/#routine">Routine</a>
      <a href="/genuine-mumuki-india/">Genuine MUMUKI</a>
      <a href="/#faq">FAQ</a>
    </nav>
    <a href="/" class="logo">MUMUKI<small>INDIA</small></a>
    <div class="nav-right"><a href="/#notify">Join the launch list</a></div>
  </div>
</header>
'''

def foot():
    shop = ''.join(f'<li><a href="{purl(i)}">{esc(P[i]["name"].replace("Honey Banana ", ""))}</a></li>' for i in ORDER)
    learn = ''.join(f'<li><a href="{gurl(g["slug"])}">{esc(g["short"])}</a></li>' for g in GUIDES[:6]) + '<li><a href="/guides/">All PDRN guides</a></li>'
    return f'''
<div class="news">
  <span class="eyebrow" style="color:var(--ink-2)">Launching soon in India</span>
  <h2>Be the <em>first</em> to glow.</h2>
  <p>Join the launch list for early access and 10% off your first order.</p>
  <a class="btn btn-dark" href="/#notify">Join the launch list</a>
</div>
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="logo">MUMUKI<small>INDIA</small></div>
        <p style="color:var(--muted);max-width:320px;font-weight:300;font-size:14px">Honey Banana PDRN Korean skincare, imported directly from Korea and delivered across India.</p>
      </div>
      <div><h5>Shop</h5><ul>{shop}</ul></div>
      <div><h5>Learn</h5><ul>{learn}<li><a href="/genuine-mumuki-india/">Genuine MUMUKI in India</a></li></ul></div>
      <div><h5>Help</h5><ul><li><a href="/#faq">FAQ</a></li><li><a href="/shipping.html">Shipping policy</a></li><li><a href="/returns.html">Returns &amp; refunds</a></li><li><a href="/terms.html">Terms &amp; conditions</a></li><li><a href="/privacy.html">Privacy policy</a></li><li><a href="https://wa.me/{WA}">WhatsApp +91 99808 81230</a></li><li>hello@mumuki.in</li></ul></div>
    </div>
    <div class="legal">© 2026 mumuki.in · Imported &amp; marketed in India by Beauty Mart Pvt Ltd, Azad Nagar 4th Cross, Bhatkal, Uttara Kannada, Karnataka 581320</div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{WA}?text=Hi%20MUMUKI%20India!" aria-label="Chat on WhatsApp">{WA_SVG}</a>
<script>
var mb=document.getElementById('menuBtn'),nl=document.getElementById('navLinks');
mb.addEventListener('click',function(){{var o=nl.classList.toggle('open');mb.setAttribute('aria-expanded',o);}});
</script>
</body>
</html>
'''

def crumbs(items):
    parts = []
    for i, (name, url) in enumerate(items):
        parts.append(f'<a href="{url}">{esc(name)}</a>' if url and i < len(items) - 1 else esc(name))
    return '<div class="crumbs">' + '<span>/</span>'.join(parts) + '</div>'

def crumb_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + (u or '')} for i, (n, u) in enumerate(items)]}

def product_cards(ids, title='Pairs well <em>with</em>', eyebrow='Complete the routine'):
    cards = ''.join(f'''<a class="card" href="{purl(i)}"><div class="img"><img src="/{P[i]["img"]}" alt="MUMUKI {esc(P[i]["name"])}" loading="lazy"></div><span class="ln">MUMUKI</span><h3>{esc(P[i]["name"])}</h3><p>{esc(P[i]["desc"])}</p></a>''' for i in ids)
    return f'<section class="rel"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2><div class="cards">{cards}</div></div></section>'

def guide_cards(slugs, title='Learn <em>more</em>'):
    cards = ''.join(f'<a class="gcard" href="{gurl(s)}"><span class="ln">Guide</span><h3>{esc(gshort(s))}</h3><p>{esc(gblurb(s))}</p><span class="more">Read →</span></a>' for s in slugs)
    return f'<section class="rel"><div class="wrap"><span class="eyebrow">PDRN guides</span><h2>{title}</h2><div class="gcards">{cards}</div></div></section>'

def write(path, content):
    full = os.path.join(ROOT, path.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(content)

# ---------- product pages ----------
def product_page(pid):
    p, m = P[pid], META[pid]
    path = purl(pid)
    gallery = [g for g in (p.get('gallery') or [p['img']]) if os.path.exists(os.path.join(ROOT, g))] or [p['img']]
    thumbs = ''.join(f'<button type="button" class="{"on" if i == 0 else ""}" data-src="/{g}" aria-label="Photo {i + 1}"><img src="/{g}" alt="" loading="lazy"></button>' for i, g in enumerate(gallery)) if len(gallery) > 1 else ''
    feats = ''.join(f'<span>#{esc(f)}</span>' for f in (p.get('feats') or []))
    tags = ''.join(f'<span>{esc(t)}</span>' for t in (p.get('tags') or []))
    hl = ''.join(f'<li><b>{esc(clean_emoji(h[0]))}</b>{esc(h[1])}</li>' for h in p.get('highlights') or [])
    suits = ''.join(f'<li>{esc(s)}</li>' for s in m['suits'])
    ext = p.get('ext')
    ext_html = (f'<div class="ext"><span>{(str(ext["n"]) + " customer reviews") if ext.get("n") else "Customer reviews"} on MUMUKI\'s official US store</span><a href="{esc(ext["url"])}" target="_blank" rel="noopener">Read them →</a></div>') if ext else ''
    crumbs_items = [('Home', '/'), ('Shop', '/#shop'), (p['name'], path)]
    ld = {"@context": "https://schema.org", "@graph": [crumb_ld(crumbs_items),
          {"@type": "WebPage", "name": m['seo'], "url": SITE + path, "description": m['desc'], "primaryImageOfPage": SITE + '/' + p['img'],
           "about": {"@type": "Thing", "name": p['name']}, "publisher": {"@type": "Organization", "name": "MUMUKI India", "url": SITE + '/'}}]}
    msg = 'Hi MUMUKI India! I would like to order: %s. Please share price and availability.' % p['name']
    body = f'''<main class="wrap">
{crumbs(crumbs_items)}
<div class="pdp">
  <div class="pgal">
    <div class="pgal-main"><img id="pMain" src="/{gallery[0]}" alt="MUMUKI {esc(p['name'])}"></div>
    <div class="pthumbs" id="pThumbs">{thumbs}</div>
  </div>
  <div class="pinfo">
    <span class="line">MUMUKI · {esc(p['line'])}</span>
    <h1>{esc(p['name'])}</h1>
    <div class="feats">{feats}</div>
    <p class="lead">{esc(p['desc'])}</p>
    <div class="tags">{tags}</div>
    <div class="cta">
      <a class="wa-btn" href="{wa_link(msg)}" target="_blank" rel="noopener"><span class="wa-ico">{WA_SVG}</span><span>Order on WhatsApp</span><span class="arrow">→</span></a>
      <span class="note">Ask for the current price and availability. Cash on delivery available on most pin codes. <a href="/#notify" style="border-bottom:1px solid currentColor">Join the launch list</a> for 10% off your first order.</span>
    </div>
    {ext_html}
    <h2>Key ingredients (as described by MUMUKI)</h2>
    <ul class="hl">{hl}</ul>
    <p class="note" style="font-size:12.5px;color:var(--muted)">Ingredient benefits, amounts and test results are the brand's own descriptions.</p>
    <h2>How to use</h2>
    <p>{esc(p['howto'])}</p>
    <h2>Who it suits</h2>
    <ul class="plain">{suits}</ul>
    <h2>Good to know</h2>
    <ul class="plain">
      <li>Patch test behind the ear or on the inner arm for 24 to 48 hours before first use.</li>
      <li>Check the full ingredient list on the pack. Some MUMUKI products list retinol, and hydrolysed collagen whose source the brand does not state. If you are pregnant or breastfeeding, have a fish allergy or are vegetarian, message us before buying.</li>
      <li>Wear sunscreen every morning; it protects the results of any routine.</li>
      <li>Imported from Korea and sold in India by Beauty Mart Pvt Ltd, with an Indian importer label showing batch, MRP and expiry. See <a href="/genuine-mumuki-india/" style="border-bottom:1px solid currentColor">how to check a genuine pack</a>.</li>
      <li>New to PDRN? Read <a href="/guides/what-is-pdrn/" style="border-bottom:1px solid currentColor">what PDRN is</a> and <a href="/guides/plant-pdrn-vs-salmon-pdrn/" style="border-bottom:1px solid currentColor">how banana BDRN compares with salmon PDRN</a>.</li>
    </ul>
    <p class="fine">Made in South Korea · Fragrance-free · Patch test before first use</p>
  </div>
</div>
</main>
{product_cards(m['pairs'])}
{guide_cards(m['guides'])}
<script>
document.querySelectorAll('#pThumbs button').forEach(function(b){{b.addEventListener('click',function(){{
  document.getElementById('pMain').src=b.dataset.src;document.querySelectorAll('#pThumbs button').forEach(function(x){{x.classList.toggle('on',x===b);}});}});}});
</script>'''
    write(path, head(m['seo'], m['desc'], path, '/' + p['img'], ld) + body + foot())
    return path

# ---------- guide pages ----------
def article_page(g, path, crumbs_items, products, related):
    faq_html = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in g.get('faq', []))
    refs = g.get('refs', [])
    refs_html = ('<div class="refs"><h4>Sources</h4><ol>' + ''.join(f'<li><a href="{REFS[r][1]}" rel="noopener">{esc(REFS[r][0])}</a></li>' for r in refs) + '</ol></div>') if refs else ''
    pick = ''
    if products:
        pid = products[0]
        pick = f'<a class="pick" href="{purl(pid)}"><img src="/{P[pid]["img"]}" alt="" loading="lazy"><div><span class="t">From MUMUKI</span><h4>{esc(P[pid]["name"])}</h4><p>{esc(P[pid]["desc"])}</p></div></a>'
    body_html = g['body']
    # place the product pick after the second section
    parts = body_html.split('<h2>')
    if len(parts) > 3:
        body_html = '<h2>'.join(parts[:3]) + pick + '<h2>' + '<h2>'.join(parts[3:])
    else:
        body_html += pick
    seo_title = g['seo']
    h1_plain = plain(g['title'])
    ld_items = [crumb_ld(crumbs_items),
                {"@type": "Article", "headline": h1_plain, "description": g['desc'], "datePublished": UPDATED, "dateModified": UPDATED,
                 "author": {"@type": "Organization", "name": "MUMUKI India", "url": SITE + '/'},
                 "publisher": {"@type": "Organization", "name": "MUMUKI India", "logo": {"@type": "ImageObject", "url": SITE + "/images/logo-512.png"}},
                 "mainEntityOfPage": SITE + path, "image": SITE + '/' + (P[products[0]]['img'] if products else 'images/share.jpg')}]
    if g.get('faq'):
        ld_items.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g['faq']]})
    ld = {"@context": "https://schema.org", "@graph": ld_items}
    content = f'''<main class="wrap">
{crumbs(crumbs_items)}
<article class="art">
  <span class="eyebrow">{'PDRN guide' if path.startswith('/guides/') else 'Buying guide'}</span>
  <h1>{g['title']}</h1>
  <p class="dek">{esc(g['dek'])}</p>
  <p class="by">By the MUMUKI India team · Updated {UPDATED_TEXT}</p>
  <div class="answer"><b>Short answer</b><p>{esc(g['answer'])}</p></div>
  {body_html}
  {'<h2>Frequently asked questions</h2><div class="faqs">' + faq_html + '</div>' if faq_html else ''}
  {refs_html}
  <p class="disclaimer">This guide is general skincare information, not medical advice. For skin conditions, allergies, pregnancy or injections, speak to a dermatologist.</p>
</article>
</main>
{product_cards(products, title='Shop the <em>routine</em>', eyebrow='From MUMUKI') if products else ''}
{guide_cards(related, title='Keep <em>reading</em>') if related else ''}'''
    image = '/' + (P[products[0]]['img'] if products else 'images/share.jpg')
    write(path, head(seo_title, g['desc'], path, image, ld) + content + foot())
    return path

def hub_page():
    path = '/guides/'
    items = [('Home', '/'), ('PDRN guides', path)]
    allg = GUIDES + [GENUINE]
    cards = ''.join(f'<a class="gcard" href="{gurl(g["slug"])}"><span class="ln">Guide</span><h3>{esc(g["short"])}</h3><p>{esc(g["dek"])}</p><span class="more">Read →</span></a>' for g in allg)
    desc = 'PDRN skincare guides for India: what PDRN is, plant vs salmon PDRN, benefits, safety, how to use it, prices in India and a glass-skin routine.'
    ld = {"@context": "https://schema.org", "@graph": [crumb_ld(items), {"@type": "CollectionPage", "name": "PDRN skincare guides", "url": SITE + path, "description": desc,
          "hasPart": [{"@type": "Article", "headline": plain(g['title']), "url": SITE + gurl(g['slug'])} for g in allg]}]}
    content = f'''<main class="wrap">
{crumbs(items)}
<div class="hub-head"><span class="eyebrow">Learn</span><h1>PDRN skincare, <em>explained</em></h1><p>Plain, honest guides to PDRN and Korean skincare for Indian skin and weather, from the MUMUKI India team.</p></div>
<div class="gcards" style="padding-bottom:90px">{cards}</div>
</main>
{product_cards([1, 2, 14, 10], title='The Honey Banana <em>collection</em>', eyebrow='From MUMUKI')}'''
    write(path, head('PDRN Skincare Guides for India | MUMUKI India', desc, path, '/images/share.jpg', ld) + content + foot())
    return path

def sitemap(paths):
    urls = ['/', '/shipping.html', '/returns.html', '/terms.html', '/privacy.html'] + paths
    body = ''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{UPDATED}</lastmod></url>\n' for u in urls)
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + '</urlset>\n')

if __name__ == '__main__':
    P = {p['id']: p for p in load_products()}
    missing = [i for i in ORDER if i not in P]
    if missing: sys.exit('products missing from index.html: %s' % missing)
    paths = [product_page(i) for i in ORDER]
    paths.append(hub_page())
    for g in GUIDES:
        paths.append(article_page(g, gurl(g['slug']), [('Home', '/'), ('PDRN guides', '/guides/'), (g['short'], gurl(g['slug']))], g.get('products', []), g.get('related', [])))
    paths.append(article_page(GENUINE, '/genuine-mumuki-india/', [('Home', '/'), (GENUINE['short'], '/genuine-mumuki-india/')], [10], ['pdrn-serum-price-in-india', 'what-is-pdrn', 'is-pdrn-safe']))
    sitemap(paths)
    print('built %d pages' % len(paths))
