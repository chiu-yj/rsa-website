/* RSA lightweight public-site interactions. No tracking or external dependencies. */
(()=>{"use strict";
 const menu=document.querySelector("[data-menu-toggle]");
 const mobile=document.querySelector("[data-mobile-nav]");
 if(menu&&mobile){
   function close(){menu.setAttribute("aria-expanded","false");mobile.hidden=true;}
   menu.addEventListener("click",()=>{const open=menu.getAttribute("aria-expanded")==="true";menu.setAttribute("aria-expanded",String(!open));mobile.hidden=open;});
   mobile.querySelectorAll("a").forEach(a=>a.addEventListener("click",close));
   document.addEventListener("keydown",e=>{if(e.key==="Escape")close();});
   const mq=window.matchMedia("(min-width: 841px)");
   if(mq.addEventListener)mq.addEventListener("change",()=>{if(mq.matches)close();});
 }
 const lightbox=document.querySelector("[data-lightbox]");
 if(lightbox){
   const image=lightbox.querySelector("img"),caption=lightbox.querySelector("[data-lightbox-caption]");
   const closeButton=lightbox.querySelector("[data-lightbox-close]");
   let opener=null;
   function close(){lightbox.hidden=true;document.body.classList.remove("modal-open");image.removeAttribute("src");if(opener)opener.focus();}
   document.querySelectorAll("[data-enlarge]").forEach(button=>button.addEventListener("click",()=>{
     opener=button;image.src=button.dataset.enlarge;image.alt=button.dataset.alt||"RSA prototype screenshot";
     caption.textContent=button.dataset.caption||"Research prototype";lightbox.hidden=false;document.body.classList.add("modal-open");closeButton.focus();
   }));
   closeButton.addEventListener("click",close);
   lightbox.addEventListener("click",e=>{if(e.target===lightbox)close();});
   document.addEventListener("keydown",e=>{if(e.key==="Escape"&&!lightbox.hidden)close();});
 }
})();
