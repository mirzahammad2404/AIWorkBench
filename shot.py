import http.server,threading,functools
from playwright.sync_api import sync_playwright
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(s,*a):pass
srv=http.server.ThreadingHTTPServer(("127.0.0.1",8765),functools.partial(Q,directory="dist"));threading.Thread(target=srv.serve_forever,daemon=True).start()
pages=["/","/prompts/","/video-prompts/","/picture-prompts/","/blog/","/about/","/contact/","/privacy-policy/","/how-to-write-better-ai-prompts/"]
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,vp in(("m",{"width":375,"height":780}),("d",{"width":1100,"height":900})):
        pg=b.new_page(viewport=vp)
        for u in pages:
            pg.goto("http://127.0.0.1:8765"+u);pg.wait_for_timeout(250)
            sw=pg.evaluate("[document.documentElement.scrollWidth,innerWidth]")
            if sw[0]>sw[1]:print("OVERFLOW",name,u,sw)
        if name=="m":
            pg.context.grant_permissions(["clipboard-read","clipboard-write"])
            pg.goto("http://127.0.0.1:8765/video-prompts/");pg.click(".copy >> nth=1");pg.wait_for_timeout(300);print("toast:",pg.inner_text("#toast"))
            print("copied starts:",pg.evaluate("navigator.clipboard.readText()").then if False else "")
        if name=="d":
            pg.goto("http://127.0.0.1:8765/video-prompts/");pg.wait_for_timeout(500);pg.screenshot(path="/tmp/vp_d.png")
            pg.goto("http://127.0.0.1:8765/prompts/");pg.screenshot(path="/tmp/hub_d.png")
    b.close()
print("done")
