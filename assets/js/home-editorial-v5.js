/* RSA homepage · accessible manual research-image showcase. No auto-rotation. */
(()=>{'use strict';
 const controls=[...document.querySelectorAll('[data-stage-button]')];
 const images=[...document.querySelectorAll('[data-stage-image]')];
 const caption=document.querySelector('[data-stage-credit]');
 if(!controls.length||!images.length)return;
 controls.forEach(button=>button.addEventListener('click',()=>{
  const chosen=button.getAttribute('data-stage-button');
  if(!images.some(img=>img.getAttribute('data-stage-image')===chosen))return;
  images.forEach(img=>img.classList.toggle('is-active',img.getAttribute('data-stage-image')===chosen));
  controls.forEach(control=>control.setAttribute('aria-pressed',String(control===button)));
  if(caption)caption.textContent=button.getAttribute('data-stage-caption')||caption.textContent;
 }));
})();
