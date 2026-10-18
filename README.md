# AI Workbench
Static SEO site. `python build.py` builds /dist. Netlify runs this automatically.
- Add posts: edit POSTS in build.py. Cover images: put `images/<slug>.webp` in /images.
- Edit page text: pages.py
- AdSense: after approval set ADSENSE in build.py (adds script + ads.txt).
- Contact form uses Netlify Forms (enable form notifications in Netlify > Forms).
- Custom domain: add it in Netlify; the build picks it up automatically.
