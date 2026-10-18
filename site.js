(function(){var b=document.getElementById('bg'),n=document.getElementById('nv');
if(b)b.onclick=function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)};
var c=document.getElementById('cp');if(c)c.onclick=function(){var t=document.getElementById('pt').textContent;
(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){c.textContent='Copied'},function(){c.textContent='Select and copy'});
setTimeout(function(){c.textContent='Copy prompt'},1800)};
var q=document.getElementById('q');if(q)q.oninput=function(){var v=q.value.toLowerCase();
document.querySelectorAll('#gr .card').forEach(function(x){x.style.display=x.textContent.toLowerCase().indexOf(v)>-1?'':'none'})}})();
