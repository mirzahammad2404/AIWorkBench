(function(){
var b=document.getElementById('bg'),n=document.getElementById('nv'),t=document.getElementById('toast'),tm;
function toast(m,err){if(!t)return;t.textContent=m;t.className='toast show'+(err?' err':'');clearTimeout(tm);tm=setTimeout(function(){t.className='toast'},3200)}
function setMenu(o){n.classList.toggle('open',o);b.setAttribute('aria-expanded',o);b.lastChild.textContent=o?'Close':'Menu'}
if(b){b.onclick=function(){setMenu(!n.classList.contains('open'))};n.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')setMenu(false)});
document.addEventListener('click',function(e){if(!e.target.closest('.hd'))setMenu(false)})}
document.querySelectorAll('.copy').forEach(function(c){c.onclick=function(){var p=document.getElementById(c.dataset.for),x=p.textContent;
var ok=function(){toast('Prompt copied! Paste it into your AI tool.')};
var no=function(){var r=document.createRange();r.selectNodeContents(p);var s=getSelection();s.removeAllRanges();s.addRange(r);toast('Could not copy automatically. The prompt is selected, press Ctrl+C (or Copy).',1)};
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(x).then(ok,no)}else no()}});
var q=document.getElementById('q'),fc=document.getElementById('fc'),ty='';
function filt(){var v=q?q.value.toLowerCase():'',k=0;document.querySelectorAll('#gr .card').forEach(function(x){var s=(!ty||x.dataset.type===ty)&&x.textContent.toLowerCase().indexOf(v)>-1;x.style.display=s?'':'none';if(s)k++});
var e=document.getElementById('none');if(e)e.hidden=k>0}
if(q)q.oninput=filt;
if(fc)fc.onclick=function(ev){var b=ev.target.closest('.chip');if(!b)return;fc.querySelectorAll('.chip').forEach(function(c){c.classList.remove('on');c.setAttribute('aria-pressed','false')});b.classList.add('on');b.setAttribute('aria-pressed','true');ty=b.dataset.t;filt()};
var f=document.querySelector('form[data-netlify]'),m=document.getElementById('fm');
if(f&&window.fetch)f.addEventListener('submit',function(e){e.preventDefault();var s=f.querySelector('button');s.disabled=true;s.textContent='Sending...';
fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(new FormData(f)).toString()})
.then(function(r){if(!r.ok)throw 0;f.reset();m.className='fmsg ok';m.textContent='Thanks! Your message was sent. We will reply soon.'})
.catch(function(){m.className='fmsg err';m.textContent='Sorry, your message did not send. Please try again, or email us directly.'})
.finally(function(){s.disabled=false;s.textContent='Send message'})});
})();
