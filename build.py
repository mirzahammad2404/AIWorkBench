#!/usr/bin/env python3
"""AI Workbench static site builder. `python build.py` -> /dist (Netlify runs this automatically).
Content: posts.py (prompts and guides), pages.py (page text). Covers: images/<slug>.webp"""
import os, re, shutil, json, html
from datetime import date
import pages as P
from posts import POSTS

SITE = os.environ.get("URL", "https://aiworkbenches.tech").rstrip("/")
THEME = "candle"            # "candle" (cream, coral, leaf, juniper) or "fresh" (white, blue, orange, navy)
NAME = "AI Workbench"
TAG = "Free AI prompts, tool guides and tutorials."
PHONE, PHONE_SHOW, EMAIL = "+923042226961", "+92 304 2226961", "hammadonline2404@gmail.com"
SOCIAL = {}                 # add real links, e.g. {"TikTok": "https://tiktok.com/@yourhandle"}
PREF = "https://www.google.com/preferences/source?q=aiworkbenches.tech"   # Google Preferred Sources link
ADSENSE = ""                # after approval: "ca-pub-XXXXXXXXXXXXXXXX"

e = html.escape
OUT = "dist"
CSS = re.sub(r"\n\s*", "", open("style.css", encoding="utf-8").read())
FONT = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&amp;family=DM+Sans:wght@400;500;700&amp;display=swap"
PT = {"Video": ("video-prompts", "Video Prompts"), "Image": ("picture-prompts", "Picture Prompts")}
PROMPT_PATHS = ["/prompts/"] + [f"/{v[0]}/" for v in PT.values()]
NOINDEX = {"/thank-you/", "/404"}
NAV = [("/", "Home"), ("/prompts/", "AI Prompts"), ("/blog/", "Blog"), ("/about/", "About"), ("/contact/", "Contact")]

def img_for(slug):
    for ext in ("webp", "jpg", "jpeg", "png"):
        if os.path.exists(f"images/{slug}.{ext}"):
            return f"/images/{slug}.{ext}"
    return ""

def head(title, desc, path, og="", extra=""):
    url = SITE + path
    full = title if title.startswith(NAME) or len(title) + len(NAME) + 3 > 60 else f"{title} | {NAME}"
    img = SITE + (og or "/og-default.png")
    robots = "noindex,follow" if path in NOINDEX else "index,follow,max-image-preview:large"
    ads = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE}" crossorigin="anonymous"></script>' if ADSENSE else ""
    links = "".join(f'<a href="{u}"' + (' aria-current="page"' if (u == path or (u == "/prompts/" and path in PROMPT_PATHS)) else "") + f">{t}</a>" for u, t in NAV)
    return f"""<!doctype html><html lang="en" data-theme="{THEME}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(full)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}"><meta name="robots" content="{robots}">
<meta name="theme-color" content="#FBF5E9"><link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}"><meta property="og:title" content="{e(full)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{FONT}" onload="this.onload=null;this.rel='stylesheet'"><noscript><link rel="stylesheet" href="{FONT}"></noscript>
<style>{CSS}</style><script async src="https://news.google.com/swg/js/v1/publisher.js"></script>{ads}{extra}</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="hd"><div class="w bar"><a class="logo" href="/" aria-label="{NAME} home"><i>W</i>{NAME}</a>
<button class="bg" id="bg" aria-label="Open menu" aria-expanded="false" aria-controls="nv"><span aria-hidden="true">&#9776;</span><span>Menu</span></button>
<nav id="nv" aria-label="Main">{links}<a class="btn sm" href="/prompts/">Free prompts</a></nav></div></header><main id="main">"""

def foot():
    soc = "".join(f'<a href="{u}" rel="noopener">{n}</a>' for n, u in SOCIAL.items())
    return f"""</main><footer class="ft"><div class="w fg"><div><b>{NAME}</b><p>{TAG}</p><div class="pbadge"><div google-add-preferred-source-btn data-theme="light" data-lang="en"></div></div></div>
<div><b>Quick links</b>{''.join(f'<a href="{u}">{t}</a>' for u, t in NAV)}</div>
<div><b>Legal</b><a href="/privacy-policy/">Privacy policy</a><a href="/terms-and-conditions/">Terms and conditions</a><a href="/disclaimer/">Disclaimer</a></div>
<div><b>Contact</b><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE}">{PHONE_SHOW}</a>{soc}</div></div>
<div class="w cp">&copy; {date.today().year} {NAME}. All rights reserved. Some links may be affiliate links.</div></footer>
<div id="toast" class="toast" role="status" aria-live="polite"></div><script src="/site.js" defer></script></body></html>"""

def ld(o): return f'<script type="application/ld+json">{json.dumps(o)}</script>'
def label(p): return f'{p["ptype"]} prompt' if p.get("ptype") else p["cat"]
def href(p): return f"/{PT[p['ptype']][0]}/#{p['slug']}" if p["kind"] == "prompt" else f"/{p['slug']}/"

def card(p):
    im = img_for(p["slug"]); alt = e(p.get("alt", p["title"]))
    pic = f'<img src="{im}" alt="{alt}" width="640" height="360" loading="lazy">' if im else f'<div class="ph" style="--h:{p.get("hue", 150)}"></div>'
    u = href(p)
    return f'<article class="card" data-type="{p.get("ptype", "")}"><a href="{u}" class="cvr" tabindex="-1" aria-hidden="true">{pic}</a><div class="cb"><span class="tag">{e(label(p))}</span><h3><a href="{u}">{e(p["title"])}</a></h3><p>{e(p["intro"][:115].rsplit(" ", 1)[0])}...</p><a class="more" href="{u}">Read more<span class="sr"> about {e(p["title"])}</span></a></div></article>'

def pcard(p):
    im = img_for(p["slug"]); alt = e(p.get("alt", p["title"]))
    pic = f'<img src="{im}" alt="{alt}" width="640" height="360" loading="lazy">' if im else f'<div class="ph" style="--h:{p.get("hue", 150)}"></div>'
    pv = " ".join(p["prompt"].split())
    if len(pv) > 200: pv = pv[:200].rsplit(" ", 1)[0] + "..."
    return f'<article class="card pc" id="{p["slug"]}" data-type="{p.get("ptype", "")}"><div class="cvr">{pic}</div><div class="cb"><span class="tag">{e(label(p))}</span><h3>{e(p["title"])}</h3><p class="pv"><span>{e(pv)}</span></p><div class="row"><button class="btn copy" data-slug="{p["slug"]}" type="button">Copy prompt<span class="sr"> for {e(p["title"])}</span></button></div></div></article>'

def crumbs(items):
    lis = "".join(f'<li><a href="{u}">{t}</a></li>' if u else f"<li>{t}</li>" for t, u in items)
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": t, "item": SITE + u} for i, (t, u) in enumerate(items) if u]}
    return f'<nav class="crumb" aria-label="Breadcrumb"><ol>{lis}</ol></nav>', ld(data)

def write(path, content):
    d = os.path.join(OUT, path.strip("/")); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(content)

def listing(title, h1, desc, path, items, intro):
    bc, bcj = crumbs([("Home", "/"), (h1, None)])
    body = f'<div class="w pg">{bc}<h1>{h1}</h1><p class="lead">{intro}</p><input id="q" class="srch" type="search" placeholder="Search {h1.lower()}" aria-label="Search {h1.lower()}"><div class="grid" id="gr">{"".join(card(p) for p in items) or "<p>New posts are coming soon.</p>"}</div><p id="none" hidden>No results found. Try a different word.</p></div>'
    write(path, head(title, desc, path, extra=bcj) + body + foot())

def simple(path, title, h1, desc, body):
    bc, bcj = crumbs([("Home", "/"), (h1, None)])
    write(path, head(title, desc, path, extra=bcj) + f'<div class="w pg narrow">{bc}<h1>{h1}</h1>{body}</div>' + foot())

PBAND = '<section class="w sec"><div class="pband"><div><h2>Add AI Workbench to your Google results</h2><p>Find our prompts useful? Choose AI Workbench as a preferred source in Google. You may then see our pages more often in Top Stories and in AI answers on Google. It takes two taps, and you need to be signed in to Google.</p></div><div google-add-preferred-source-btn data-theme="light" data-lang="en"></div></div></section>'

def faqblock(f):
    return '<section class="w sec faqsec"><h2>Frequently asked questions</h2>' + "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in f) + "</section>"

HUBTXT = {"Video": "Copy-and-paste prompts for AI video tools: 3D animated reels, character swaps and more.", "Image": "Copy-and-paste prompts for AI image tools: posters, characters and scenes."}
CAT = {"Video": ("Free AI Video Prompts", "Free AI Video Prompts for Reels, Shorts and Edits", "Free AI video prompts you can copy and paste: 3D animated comedy reels, character swap edits and more for TikTok, Instagram Reels and YouTube Shorts.", "Copy-and-paste AI video prompts for TikTok, Instagram Reels and YouTube Shorts. Tap Copy prompt on any card, paste it into your AI tool and start creating.", '<h2>How to use AI video prompts</h2><ol><li>Pick a prompt and tap <strong>Copy prompt</strong>.</li><li>Paste it into your AI tool and replace anything in [brackets].</li><li>Generate a short test, then refine it and run the full video.</li><li>Edit the clip, add your cover image and post.</li></ol>'),
       "Image": ("Free AI Picture Prompts", "Free AI Picture Prompts for Posters and Images", "Free AI picture prompts you can copy and paste to create posters, characters and scenes. New prompts are added regularly.", "Copy-and-paste AI picture prompts for posters, characters and scenes.", "")}
CATFAQ = {"Video": [("What is an AI video prompt?", "An AI video prompt is the text instruction you give an AI tool to create or edit a video. A clear prompt that describes the scene, characters, camera and style gives better results."), ("Are these AI video prompts free?", "Yes. Every prompt on AI Workbench is free to copy and use."), ("Which AI tools can I use these prompts with?", "Most prompts work with popular AI video and chat tools. Each prompt names the type of tool it is made for.")],
          "Image": [("What is an AI picture prompt?", "An AI picture prompt is the text instruction you give an AI image tool to create a picture. Describing the subject, style, lighting and mood gives better results."), ("Are these AI picture prompts free?", "Yes. Every prompt on AI Workbench is free to copy and use.")]}

def hub(prompts):
    bc, bcj = crumbs([("Home", "/"), ("AI Prompts", None)])
    cards = ""
    for t, (slug, name) in PT.items():
        n = len([p for p in prompts if p.get("ptype") == t])
        status = f"{n} prompt{'s' if n != 1 else ''}" if n else "Coming soon"
        cards += f'<a class="hubcard" href="/{slug}/"><span class="tag">{status}</span><h2>{name}</h2><p>{HUBTXT[t]}</p><span class="more">Browse {name.lower()}</span></a>'
    body = f'<div class="w pg">{bc}<h1>AI Prompts</h1><p class="lead">Free AI prompts you can copy, paste and use today. Choose a type to get started.</p><div class="hubgrid">{cards}</div></div>'
    write("/prompts/", head("Free AI Prompts for Video and Pictures", "Free AI prompts you can copy and paste: AI video prompts for reels and edits, and AI picture prompts for posters and images.", "/prompts/", extra=bcj) + body + foot())

def category(t, items, urls):
    slug, name = PT[t]; path = f"/{slug}/"; h1, title, desc, lead, how = CAT[t]
    bc, bcj = crumbs([("Home", "/"), ("AI Prompts", "/prompts/"), (name, None)])
    extra = bcj
    if items:
        faq = CATFAQ[t]
        extra += ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
        body = f'<input id="q" class="srch" type="search" placeholder="Search {name.lower()}" aria-label="Search {name.lower()}"><div class="grid" id="gr">{"".join(pcard(p) for p in items)}</div><p id="none" hidden>No results found. Try a different word.</p><section class="faqsec">{how}<h2>Frequently asked questions</h2>' + "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in faq) + "</section>"
        urls.append(path)
    else:
        NOINDEX.add(path)
        body = '<div class="empty">The first picture prompts are coming soon. Meanwhile, browse the <a href="/video-prompts/" style="text-decoration:underline">free AI video prompts</a>.</div>'
    write(path, head(title, desc, path, extra=extra) + f'<div class="w pg">{bc}<h1>{h1}</h1><p class="lead">{lead}</p>{body}</div>' + foot())

def main():
    shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
    shutil.copy("style.css", OUT); shutil.copy("site.js", OUT)
    if os.path.isdir("static"):
        for f in os.listdir("static"): shutil.copy(f"static/{f}", OUT)
    if os.path.isdir("images"): shutil.copytree("images", f"{OUT}/images")
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    prompts = [p for p in posts if p["kind"] == "prompt"]
    guides = [p for p in posts if p["kind"] == "post"]
    urls = ["/", "/prompts/", "/blog/", "/about/", "/contact/", "/privacy-policy/", "/terms-and-conditions/", "/disclaimer/"]

    # ---- home
    org = {"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE, "logo": SITE + "/favicon.svg", "email": EMAIL, "telephone": PHONE, "contactPoint": {"@type": "ContactPoint", "email": EMAIL, "telephone": PHONE, "contactType": "customer support"}}
    if SOCIAL: org["sameAs"] = list(SOCIAL.values())
    hj = ld({"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE}) + ld(org) + ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in P.HOME_FAQ]})
    fp = prompts[0] if prompts else None
    demo = f'<a class="demo" href="{href(fp)}" aria-label="Open prompt: {e(fp["title"])}"><span class="tag">{e(label(fp))}</span><b>{e(fp["title"].split(":")[0])}</b><span class="dp">{e(" ".join(fp["prompt"].split())[:170].rsplit(" ", 1)[0])}...</span><span class="btn sm">Get this prompt</span></a>' if fp else ""
    hero = f"""<section class="hero"><div class="w hero-grid"><div><p class="eyebrow">Free AI prompts and guides</p>
<h1>Free AI prompts you can copy, paste and use today.</h1>
<p class="lead">AI Workbench is a free library of ready-made prompts and simple guides for AI video and picture tools. Get better AI answers in less time, with no sign-up.</p>
<div class="row"><a class="btn" href="/prompts/">Browse free AI prompts</a><a class="btn ghost" href="/blog/">Read the guides</a></div>
<ul class="proof"><li>100% free</li><li>No sign-up</li><li>Copy in one tap</li></ul>
<p class="for"><b>Made for</b> content creators, freelancers, students and small business owners.</p></div>{demo}</div></section>"""
    sec = lambda h, sub, items, link, fn=card: f'<section class="w sec"><div class="sh"><div><h2>{h}</h2><p>{sub}</p></div><a href="{link}">See all<span class="sr"> {h.lower()}</span></a></div><div class="grid">{"".join(fn(p) for p in items[:6])}</div></section>'
    write("/", head(f"{NAME}: Free AI Prompts, Tools and Guides", "Free AI prompts you can copy and use for AI video and pictures, plus simple AI tool guides and tutorials for creators, freelancers and students.", "/", extra=hj) + hero + sec("Latest AI prompts", "Copy a prompt, fill in the brackets and paste it into your AI tool.", prompts, "/prompts/", pcard) + (sec("New guides and tips", "Plain-language help for getting more from AI.", guides, "/blog/") if guides else "") + P.HOME_INTRO + PBAND + faqblock(P.HOME_FAQ) + foot())

    hub(prompts)
    for t in PT: category(t, [p for p in prompts if p.get("ptype") == t], urls)
    listing("AI Blog: Guides, Tools and Tips", "Blog", "Practical AI guides, tool tips and tutorials written in simple words for beginners.", "/blog/", guides, "Step-by-step guides, tool tips and tutorials, all in simple words.")

    cbox = f'<h2>Other ways to reach us</h2><div class="cbox"><p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p><p>Phone: <a href="tel:{PHONE}">{PHONE_SHOW}</a></p></div>'
    prefb = f'<h2>Add us to your Google results</h2><p>If you find AI Workbench useful, you can <a href="{PREF}" target="_blank" rel="noopener" style="text-decoration:underline">add us as a preferred source on Google</a>. Sign in to Google, then tick the box next to our site.</p><div google-add-preferred-source-btn data-theme="light" data-lang="en"></div>'
    simple("/about/", "About Us: Our Mission and How We Work", "About AI Workbench", "AI Workbench is a free hub of AI prompts, AI tool guides and tutorials that make AI simple and useful for everyone.", P.ABOUT + prefb)
    simple("/contact/", "Contact Us", "Contact", "Contact AI Workbench with questions, prompt ideas, corrections or partnership enquiries.", P.CONTACT + cbox)
    simple("/privacy-policy/", "Privacy Policy", "Privacy Policy", "How AI Workbench collects, uses and protects information, including cookies and Google AdSense advertising.", P.PRIVACY)
    simple("/terms-and-conditions/", "Terms and Conditions", "Terms and Conditions", "The terms for using the AI Workbench website, including content use, AI output, ads and affiliate links.", P.TERMS)
    simple("/disclaimer/", "Disclaimer", "Disclaimer", "Disclaimer, affiliate disclosure and advertising disclosure for AI Workbench.", P.DISCLAIMER)
    simple("/thank-you/", "Thank You for Contacting Us", "Message sent", "Your message to AI Workbench was sent.", P.THANKS)

    # ---- guides (each gets its own page)
    for p in guides:
        path = f"/{p['slug']}/"; im = img_for(p["slug"])
        bc, bcj = crumbs([("Home", "/"), ("Blog", "/blog/"), (p["title"], None)])
        art = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "datePublished": p["date"], "dateModified": p["date"], "description": p["meta"], "author": {"@type": "Organization", "name": NAME}, "publisher": {"@type": "Organization", "name": NAME}, "mainEntityOfPage": SITE + path}
        if im: art["image"] = SITE + im
        extra = ld(art) + bcj
        if p.get("faq"):
            extra += ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
        secs = "".join(f"<h2>{h}</h2>{b}" for h, b in p["sections"])
        faq = "<h2>Frequently asked questions</h2>" + "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in p["faq"]) if p.get("faq") else ""
        cw, ch = p.get("imgwh", (1280, 720))
        cover = f'<img class="hero-img{" tall" if ch > cw else ""}" src="{im}" alt="{e(p.get("alt", p["title"]))}" width="{cw}" height="{ch}">' if im else ""
        rel = [x for x in guides if x is not p][:3]
        relh = (f'<h2>Related guides</h2><div class="grid">{"".join(card(x) for x in rel)}</div>' if rel else "") + (f'<h2 style="margin-top:44px">Free AI prompts you may like</h2><div class="grid">{"".join(pcard(x) for x in prompts[:3])}</div>' if prompts else "")
        body = f'<article class="w pg narrow">{bc}<span class="tag">{e(label(p))}</span><h1>{e(p["title"])}</h1><p class="meta">Updated <time datetime="{p["date"]}">{p["date"]}</time></p>{cover}<p class="lead">{e(p["intro"])}</p>{secs}{faq}</article><div class="w sec">{relh}</div>'
        write(path, head(p["title"], p["meta"], path, og=im, extra=extra) + body + foot()); urls.append(path)

    # ---- data, redirects, sitemap, robots, 404
    json.dump({p["slug"]: p["prompt"] for p in prompts}, open(f"{OUT}/prompts.json", "w", encoding="utf-8"), ensure_ascii=False)
    open(f"{OUT}/_redirects", "w").write("".join(f"/{p['slug']}/ {href(p)} 301\n/{p['slug']} {href(p)} 301\n" for p in prompts))
    open(f"{OUT}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}{u}</loc></url>" for u in urls) + "</urlset>")
    if ADSENSE: open(f"{OUT}/ads.txt", "w").write(f"google.com, {ADSENSE.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    open(f"{OUT}/404.html", "w", encoding="utf-8").write(head("Page not found", "This page does not exist.", "/404") + '<div class="w pg"><h1>Page not found</h1><p class="lead">That page does not exist or has moved. Try the <a href="/" style="text-decoration:underline">home page</a> or browse the <a href="/prompts/" style="text-decoration:underline">free AI prompts</a>.</p><a class="btn" href="/prompts/">Browse free AI prompts</a></div>' + foot())
    print(f"Built {len(urls)} pages | {SITE}")

main()
