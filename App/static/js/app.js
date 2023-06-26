
let navbar = document.querySelector('.header .navbar');
let menuBtn = document.querySelector('#menu-btn');


document.querySelector('#menu-btn').onclick = () =>{
 navbar.classList.toggle('active');
 menuBtn.classList.toggle('active')
   
};

           
        

const themeBtn = document.querySelector(".theme-btn");
  themeBtn.addEventListener("click", () =>{
    document.body.classList.toggle("dark-theme");
    themeBtn.classList.toggle("sun");
    localStorage.setItem("saved-theme", getCurrentTheme());
    localStorage.setItem("saved-icon", getCurrentIcon());

  });
  const getCurrentTheme = () => document.body.classList.contains("dark-theme") ? "dark" : "light";
  const getCurrentIcon = () => themeBtn.classList.contains("sun") ? "sun" : "moon";
  const savedTheme = localStorage.getItem("saved-theme");
  const savedIcon = localStorage.getItem("saved-icon");
  if(savedTheme){
    document.body.classList[savedTheme == "dark" ? "add" : "remove"] ("dark-theme");
    themeBtn.classList[savedIcon == "sun" ? "add" : "remove"] ("sun")

  }

const scrolltopBtn = document.querySelector(".scrollTotop-btn");
window.addEventListener("scroll", function()
  {
    scrolltopBtn.classList.toggle("active", window.scrollY > 500);
  });
  scrolltopBtn.addEventListener("click", () =>{
      document.body.scrollTop =0;
      document.documentElement.scrollTop = 0;


  });
  const photosModals = document.querySelectorAll(".photos-modal");
  const imgCards = document.querySelectorAll(".img-card");
  const photosCloseBtns = document.querySelectorAll(".photos-close-btn");
  var photosModal = function(modalClick){
      photosModals[modalClick].classList.add("active");

  }
  imgCards.forEach((imgCard, i) =>{
      
      imgCard.addEventListener("click", () => {
          photosModal(i);

      });

  });
  photosCloseBtns.forEach((photosCloseBtn) =>
  {
      photosCloseBtn.addEventListener("click", () =>{
          photosModals.forEach((photosModalView) =>{
              photosModalView.classList.remove("active");

          });
      });

  });


ScrollReveal({ 
            //reset: true,
            distance: '60px',
            duration:2500,
            delay: 100
   
        
       });
ScrollReveal().reveal('.home .info h2,.about-info h3, .section-title-01, .section-title-02', {delay: 500, origin: 'left'});
ScrollReveal().reveal('.home .info h3,  .info p, .btn, .about-info p ', {delay: 600, origin: 'right'});
       
ScrollReveal().reveal('.about-info h4 ', {delay: 500, origin: 'top', interval:400});
ScrollReveal().reveal('.home .icons i,  .contact-left li', {delay: 500, origin: 'left', interval:200});
ScrollReveal().reveal('.home-image ', {delay: 500, origin: 'bottom', interval:200});
ScrollReveal().reveal('.contact-column, .button-group', {delay: 500, origin: 'right', interval:200});
ScrollReveal().reveal('.img-card,', {delay: 500, origin: 'left', interval:200});
ScrollReveal().reveal('.about-image, .element-item  ', {delay: 500, origin: 'left', interval:200});
ScrollReveal().reveal('.course-description, .contact-card, .education-list, .contact-left h2', {delay: 500, origin: 'left'});

ScrollReveal().reveal('footer, .box-container', {delay: 500, origin: 'top', interval:200});

ScrollReveal().reveal('.service-card, .img-card', {delay: 600, origin: 'bottom', interval:200});
      
   
       
   


init_mathjax = function() {
    if (window.MathJax) {
    // MathJax loaded
        MathJax.Hub.Config({
            TeX: {
                equationNumbers: {
                autoNumber: "AMS",
                useLabelIds: true
                }
            },
            tex2jax: {
                inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                processEscapes: true,
                processEnvironments: true
            },
            displayAlign: 'center',
            CommonHTML: {
                linebreaks: { 
                automatic: true 
                }
            }
        });
    
        MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    }
}
init_mathjax();

