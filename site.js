(function(){
var b=document.getElementById('bg'),n=document.getElementById('nv'),t=document.getElementById('toast'),tm;
function toast(m,err){if(!t)return;t.textContent=m;t.className='toast show'+(err?' err':'');clearTimeout(tm);tm=setTimeout(function(){t.className='toast'},3200)}
function setMenu(o){n.classList.toggle('open',o);b.setAttribute('aria-expanded',o);b.lastChild.textContent=o?'Close':'Menu'}
if(b){b.onclick=function(){setMenu(!n.classList.contains('open'))};n.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')setMenu(false)});
document.addEventListener('click',function(e){if(!e.target.closest('.hd'))setMenu(false)})}
var PD=null,ld=null;
function load(){if(!ld)ld=fetch('/prompts.json').then(function(r){return r.json()}).then(function(d){PD=d;return d});return ld}
function copyText(x){var ok=function(){toast('Prompt copied! Paste it into your AI tool.')};
var no=function(){toast('Could not copy automatically. Please try again or use another browser.',1)};
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(x).then(ok,no)}else no()}
document.querySelectorAll('.copy').forEach(function(c){c.onclick=function(){var s=c.dataset.slug;if(PD&&PD[s]){copyText(PD[s]);return}
load().then(function(d){copyText(d[s])},function(){toast('Could not load the prompt. Please refresh and try again.',1)})}});
if(document.querySelector('.copy[data-slug]'))setTimeout(load,600);
var q=document.getElementById('q');
if(q)q.oninput=function(){var v=q.value.toLowerCase(),k=0;document.querySelectorAll('#gr .card').forEach(function(x){var s=x.textContent.toLowerCase().indexOf(v)>-1;x.style.display=s?'':'none';if(s)k++});
var e=document.getElementById('none');if(e)e.hidden=k>0};
var f=document.querySelector('form[data-netlify]'),m=document.getElementById('fm');
if(f&&window.fetch)f.addEventListener('submit',function(e){e.preventDefault();var s=f.querySelector('button');s.disabled=true;s.textContent='Sending...';
fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(new FormData(f)).toString()})
.then(function(r){if(!r.ok)throw 0;f.reset();m.className='fmsg ok';m.textContent='Thanks! Your message was sent. We will reply soon.'})
.catch(function(){m.className='fmsg err';m.textContent='Sorry, your message did not send. Please try again, or email us directly.'})
.finally(function(){s.disabled=false;s.textContent='Send message'})});
})();
