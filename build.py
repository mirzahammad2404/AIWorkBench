#!/usr/bin/env python3
"""AI Workbench static site builder. Run: python build.py  -> creates /dist (deploy to Netlify).
Add content in POSTS below. Drop cover images in /images named <slug>.webp (or .jpg/.png)."""
import os, shutil, json, html
from datetime import date

import pages as P
SITE = os.environ.get("URL", "https://ai-workbench.netlify.app").rstrip("/")  # Netlify sets URL automatically (custom domain when connected)
ADSENSE = ""  # after approval, put your publisher id here, e.g. "ca-pub-1234567890123456"
NAME = "AI Workbench"
TAG = "Your AI workspace: prompts, tools and practical guides."
SOCIAL = {"TikTok": "https://tiktok.com/@yourhandle", "Instagram": "https://instagram.com/yourhandle", "Facebook": "https://facebook.com/yourpage"}


# kind: "prompt" or "post". Each section = (h2, html body). faq = [(question, answer)]
POSTS = [
 {"slug": "chatgpt-cold-email-prompt", "kind": "prompt", "cat": "Marketing", "date": "2026-10-19", "hue": 262,
  "title": "ChatGPT Cold Email Prompt: Get More Replies in 2026",
  "meta": "Copy this free ChatGPT cold email prompt to rewrite any pitch into a short, human message that gets replies. Includes tips and examples.",
  "intro": "Most cold emails fail because they are long and about the sender. This free ChatGPT prompt rewrites your draft so it is short, specific and easy to answer.",
  "prompt": "Act as a senior copywriter. Rewrite my cold email in under 90 words. Open with something specific about the reader, explain my offer in one sentence, and end with one easy yes/no question. Keep a friendly tone and avoid buzzwords.\n\nMy draft:\n[paste your draft]",
  "sections": [
   ("How to use this prompt", "<p>Paste the prompt into ChatGPT, Gemini or Claude, then replace the brackets with your own draft. Add the reader's job title and one detail about their company for better results.</p>"),
   ("Why this prompt works", "<p>It gives the AI a role, a word limit and a clear ending. These three prompt engineering basics make the answer shorter and more useful.</p>"),
  ],
  "faq": [("Which AI tool works best for cold emails?", "ChatGPT, Gemini and Claude all work. Pick the one you already use and keep the same prompt.")]},
 {"slug": "how-to-write-better-ai-prompts", "kind": "post", "cat": "Guides", "date": "2026-10-19", "hue": 190,
  "title": "How to Write Better AI Prompts: 4 Simple Habits",
  "meta": "Learn how to write better AI prompts with four simple habits: role, goal, context and format. Beginner friendly, with examples.",
  "intro": "A prompt is the instruction you give an AI tool. Clear prompts get clear answers. Here are four habits that improve almost every result.",
  "sections": [
   ("1. Give the AI a role", "<p>Start with who the AI should be, for example a tutor, editor or marketer.</p>"),
   ("2. State the goal", "<p>Say exactly what you want back, such as five headlines or a one-page plan.</p>"),
   ("3. Add context", "<p>Share your audience, topic and limits so the AI does not guess.</p>"),
   ("4. Ask for a format", "<p>Request a list, table or word count. Formatting rules save editing time.</p>"),
  ],
  "faq": [("What is a prompt in AI?", "A prompt is the text instruction you type into an AI tool to get an answer, image or video.")]},
]

# ------------------------------------------------------------------ build
e = html.escape
OUT = "dist"
NAV = [("/", "Home"), ("/prompts/", "AI Prompts"), ("/blog/", "Blog"), ("/about/", "About"), ("/contact/", "Contact")]

def img_for(slug):
    for ext in ("webp", "jpg", "jpeg", "png"):
        if os.path.exists(f"images/{slug}.{ext}"):
            return f"/images/{slug}.{ext}"
    return ""

def head(title, desc, path, og="", extra=""):
    url = SITE + path
    full = title if title.startswith(NAME) else f"{title} | {NAME}"
    og = og or ""
    ads = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE}" crossorigin="anonymous"></script>' if ADSENSE else ""
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(full)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large"><meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(full)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
{f'<meta property="og:image" content="{SITE}{og}"><meta name="twitter:card" content="summary_large_image">' if og else ''}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">{ads}{extra}</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="hd"><div class="w bar"><a class="logo" href="/"><i>W</i>{NAME}</a><button class="bg" id="bg" aria-label="Menu" aria-expanded="false">&#9776;</button>
<nav id="nv" aria-label="Main">{''.join(f'<a href="{u}"' + (' aria-current="page"' if u == path else '') + f'>{t}</a>' for u, t in NAV)}<a class="btn sm" href="{SOCIAL['TikTok']}" rel="noopener">Watch on TikTok</a></nav></div></header><main id="main">"""

def foot():
    soc = "".join(f'<a href="{u}" rel="noopener">{n}</a>' for n, u in SOCIAL.items())
    return f"""</main><footer class="ft"><div class="w fg"><div><b>{NAME}</b><p>{TAG}</p><p><a href="/contact/">Contact us</a></p></div>
<div><b>Quick links</b>{''.join(f'<a href="{u}">{t}</a>' for u, t in NAV)}</div>
<div><b>Legal</b><a href="/privacy-policy/">Privacy policy</a><a href="/terms-and-conditions/">Terms and conditions</a><a href="/disclaimer/">Disclaimer</a></div>
<div><b>Follow</b>{soc}</div></div><div class="w cp">&copy; {date.today().year} {NAME}. Some links may be affiliate links.</div></footer><script src="/site.js" defer></script></body></html>"""

def ld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'

def card(p):
    im = img_for(p["slug"])
    pic = f'<img src="{im}" alt="{e(p["title"])}" width="640" height="360" loading="lazy">' if im else f'<div class="ph" style="--h:{p["hue"]}"></div>'
    return f'<article class="card"><a href="/{p["slug"]}/" class="cvr">{pic}</a><div class="cb"><span class="tag">{e(p["cat"])}</span><h3><a href="/{p["slug"]}/">{e(p["title"])}</a></h3><p>{e(p["intro"][:110])}...</p><a class="more" href="/{p["slug"]}/">Read more</a></div></article>'

def crumbs(items):
    lis = "".join(f'<li><a href="{u}">{t}</a></li>' if u else f"<li>{t}</li>" for t, u in items)
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": t, "item": SITE + (u or "")} for i, (t, u) in enumerate(items) if u]}
    return f'<nav class="crumb" aria-label="Breadcrumb"><ol>{lis}</ol></nav>', ld(data)

def faqblock(f):
    return '<section class="w sec narrow-sec"><h2>Frequently asked questions</h2>' + "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in f) + "</section>"

def write(path, content):
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(content)

def listing(title, h1, desc, path, items, intro):
    bc, bcj = crumbs([("Home", "/"), (h1, None)])
    body = f'<div class="w pg">{bc}<h1>{h1}</h1><p class="lead">{intro}</p><input id="q" class="srch" type="search" placeholder="Search {h1.lower()}" aria-label="Search"><div class="grid" id="gr">{"".join(card(p) for p in items) or "<p>New posts are coming soon.</p>"}</div></div>'
    write(path, head(title, desc, path, extra=bcj) + body + foot())

def simple(path, title, h1, desc, body):
    bc, bcj = crumbs([("Home", "/"), (h1, None)])
    write(path, head(title, desc, path, extra=bcj) + f'<div class="w pg narrow">{bc}<h1>{h1}</h1>{body}</div>' + foot())

def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copy("style.css", OUT); shutil.copy("site.js", OUT)
    if os.path.isdir("images"):
        shutil.copytree("images", f"{OUT}/images")
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    prompts = [p for p in posts if p["kind"] == "prompt"]
    blog = [p for p in posts if p["kind"] == "post"]
    urls = ["/", "/prompts/", "/blog/", "/about/", "/contact/"]

    # home
    site_ld = ld({"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE}) + ld({"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE, "sameAs": list(SOCIAL.values())}) + ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in P.HOME_FAQ]})
    hero = f"""<section class="hero w"><div><p class="kick">AI prompts, tools and guides</p><h1>Your AI workspace: prompts, tools and practical guides.</h1>
<p class="lead">Discover free AI prompts, honest tool reviews and step-by-step guides that help you work smarter, in simple words.</p>
<div class="row"><a class="btn" href="/prompts/">Explore AI prompts</a><a class="btn ghost" href="/blog/">Read the blog</a></div>
<ul class="pills"><li>Free prompts</li><li>AI tools</li><li>How-to guides</li></ul></div></section>"""
    sec = lambda h, sub, items, link: f'<section class="w sec"><div class="sh"><div><h2>{h}</h2><p>{sub}</p></div><a href="{link}">See all</a></div><div class="grid">{"".join(card(p) for p in items[:6])}</div></section>'
    write("/", head(f"{NAME}: Free AI Prompts, Tools and Guides", "Free AI prompts, honest AI tool reviews and practical guides to help you work smarter with AI.", "/", extra=site_ld) + hero + sec("Latest posts", "Fresh guides and tips, explained simply.", posts, "/blog/") + sec("Free AI prompts", "Copy a prompt with one tap and use it in ChatGPT, Gemini and more.", prompts, "/prompts/") + P.HOME_INTRO + faqblock(P.HOME_FAQ) + foot())
    # lists
    listing("Free AI Prompts", "AI Prompts", "Free, ready-to-use AI prompts for ChatGPT, Gemini and more. Copy, edit the brackets and get better results.", "/prompts/", prompts, "Copy a prompt, replace the brackets with your details and paste it into your favourite AI tool.")
    listing("AI Blog: Guides, Tools and Tips", "Blog", "Practical AI guides, tool reviews and tips written in simple words.", "/blog/", posts, "Step-by-step guides, tool reviews and tips, all in simple words.")
    # pages
    simple("/about/", "About Us", "About AI Workbench", "AI Workbench is a free hub of AI prompts, AI tool guides and tutorials that make AI simple and useful for everyone.", P.ABOUT)
    simple("/contact/", "Contact Us", "Contact", "Contact AI Workbench with questions, prompt ideas, corrections or partnership enquiries.", P.CONTACT)
    simple("/privacy-policy/", "Privacy Policy", "Privacy Policy", "How AI Workbench collects, uses and protects information, including cookies and Google AdSense advertising.", P.PRIVACY)
    simple("/terms-and-conditions/", "Terms and Conditions", "Terms and Conditions", "The terms for using the AI Workbench website.", P.TERMS)
    simple("/disclaimer/", "Disclaimer", "Disclaimer", "Disclaimer, affiliate disclosure and advertising disclosure for AI Workbench.", P.DISCLAIMER)
    simple("/thank-you/", "Thank You", "Message sent", "Your message to AI Workbench was sent.", P.THANKS)
    urls += ["/privacy-policy/", "/terms-and-conditions/", "/disclaimer/"]

    # posts
    for p in posts:
        path = f"/{p['slug']}/"; im = img_for(p["slug"])
        sect = "/prompts/" if p["kind"] == "prompt" else "/blog/"
        bc, bcj = crumbs([("Home", "/"), ("AI Prompts" if p["kind"] == "prompt" else "Blog", sect), (p["title"], None)])
        art = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "datePublished": p["date"], "dateModified": p["date"], "description": p["meta"], "author": {"@type": "Organization", "name": NAME}, "publisher": {"@type": "Organization", "name": NAME}, "mainEntityOfPage": SITE + path}
        if im: art["image"] = SITE + im
        extra = ld(art) + bcj
        if p.get("faq"):
            extra += ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
        pb = f'<div class="pbox"><pre id="pt">{e(p["prompt"])}</pre><button class="btn" id="cp">Copy prompt</button></div>' if p.get("prompt") else ""
        secs = "".join(f"<h2>{h}</h2>{b}" for h, b in p["sections"])
        faq = "<h2>Frequently asked questions</h2>" + "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in p.get("faq", [])) if p.get("faq") else ""
        cover = f'<img class="hero-img" src="{im}" alt="{e(p["title"])}" width="1280" height="720">' if im else ""
        rel = [x for x in posts if x is not p][:3]
        relh = f'<h2>Related posts</h2><div class="grid">{"".join(card(x) for x in rel)}</div>' if rel else ""
        body = f'<article class="w pg narrow">{bc}<span class="tag">{e(p["cat"])}</span><h1>{e(p["title"])}</h1><p class="meta">Updated <time datetime="{p["date"]}">{p["date"]}</time></p>{cover}<p class="lead">{e(p["intro"])}</p>{pb}{secs}{faq}</article><div class="w sec">{relh}</div>'
        write(path, head(p["title"], p["meta"], path, og=im, extra=extra) + body + foot())
        urls.append(path)

    # sitemap + robots
    sm = "".join(f"<url><loc>{SITE}{u}</loc></url>" for u in urls)
    open(f"{OUT}/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>')
    if ADSENSE: open(f"{OUT}/ads.txt", "w").write(f"google.com, {ADSENSE.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print("Site URL:", SITE)
    open(f"{OUT}/404.html", "w").write(head("Page not found", "This page does not exist.", "/404") + '<div class="w pg"><h1>Page not found</h1><p class="lead">Try the <a href="/">home page</a> or browse <a href="/prompts/">AI prompts</a>.</p></div>' + foot())
    print(f"Built {len(urls)} pages into /{OUT}")

main()
