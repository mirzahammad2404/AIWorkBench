import os,re,sys
from html.parser import HTMLParser
D="dist";bad=[]
class H(HTMLParser):
    def __init__(s):super().__init__();s.l=[];s.h1=0;s.t="";s.d="";s.int=False;s.im=[]
    def handle_starttag(s,t,a):
        a=dict(a)
        if t=="a" and a.get("href"):s.l.append(a["href"])
        if t=="h1":s.h1+=1
        if t=="title":s.int=True
        if t=="meta" and a.get("name")=="description":s.d=a.get("content","")
        if t=="img" and not a.get("alt"):s.im.append(a.get("src"))
        for k in("src",):
            if t in("link","script") and a.get("href" if t=="link" else "src","").startswith("/"):s.l.append(a.get("href") or a.get("src"))
    def handle_data(s,x):
        if s.int:s.t+=x
    def handle_endtag(s,t):
        if t=="title":s.int=False
def ok(u):
    u=u.split("#")[0].split("?")[0]
    p=os.path.join(D,u.lstrip("/"))
    return os.path.isfile(p) or os.path.isfile(os.path.join(p,"index.html"))
n=0
for r,_,fs in os.walk(D):
    for f in fs:
        if not f.endswith(".html"):continue
        n+=1;path=os.path.join(r,f);s=open(path,encoding="utf-8").read();h=H();h.feed(s)
        for u in h.l:
            if u.startswith("/") and not ok(u):bad.append((path,"BROKEN",u))
            if re.search("yourhandle|yoursite|example\\.com",u):bad.append((path,"PLACEHOLDER",u))
        if h.h1!=1:bad.append((path,"H1 count",h.h1))
        if not 25<=len(h.t)<=62:bad.append((path,"title len",len(h.t),h.t))
        if not 60<=len(h.d)<=165 and "404" not in path and "thank" not in path:bad.append((path,"desc len",len(h.d)))
        if h.im:bad.append((path,"img no alt",h.im))
        if re.search("lorem|Add your|placeholder text",s,re.I):bad.append((path,"placeholder text",""))
print("pages",n,"issues",len(bad))
for b in bad:print(b)
