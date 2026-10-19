import asyncio,http.server,threading,functools,os
from playwright.sync_api import sync_playwright
h=functools.partial(http.server.SimpleHTTPRequestHandler,directory="dist")
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(s,*a):pass
srv=http.server.ThreadingHTTPServer(("127.0.0.1",8765),functools.partial(Q,directory="dist"));threading.Thread(target=srv.serve_forever,daemon=True).start()
pages=["/","/prompts/","/blog/","/about/","/contact/","/privacy-policy/","/chatgpt-cold-email-prompt/","/how-to-write-better-ai-prompts/"]
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,vp in(("m",{"width":375,"height":780}),("d",{"width":1366,"height":768})):
        pg=b.new_page(viewport=vp)
        for u in pages:
            pg.goto("http://127.0.0.1:8765"+u);pg.wait_for_timeout(300)
            sw=pg.evaluate("[document.documentElement.scrollWidth,innerWidth]")
            if sw[0]>sw[1]:print("OVERFLOW",name,u,sw)
        pg.goto("http://127.0.0.1:8765/");pg.wait_for_timeout(500);pg.screenshot(path=f"/tmp/home_{name}.png")
        if name=="m":
            pg.click("#bg");pg.wait_for_timeout(300);pg.screenshot(path="/tmp/menu_m.png")
            pg.goto("http://127.0.0.1:8765/chatgpt-cold-email-prompt/");pg.context.grant_permissions(["clipboard-read","clipboard-write"])
            pg.click("#cp");pg.wait_for_timeout(400);print("toast:",pg.inner_text("#toast"))
    b.close()
print("done")
