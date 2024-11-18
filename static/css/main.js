
    document.addEventListener("DOMContentLoaded", function () {
        const dynamicText = document.querySelector(".highlight-text");

        setTimeout(() => {
            
            dynamicText.classList.add("fade-out");
            
          
            setTimeout(() => {
                dynamicText.textContent = "Scale";
                dynamicText.classList.remove("fade-out");
                dynamicText.classList.add("fade-in");
            }, 3000);  
        }, 3000);  
    });

    


 window.addEventListener('scroll', reveal2);
 function reveal2(){
 var reveals = document.querySelectorAll('.reveal2');
 for (var i = 0; i < reveals.length; i++){
 var windowheight = window.innerHeight;
 var revealtop = reveals[i].getBoundingClientRect().top; var revealpoint = 12;
 if (revealtop < windowheight - revealpoint){ reveals[i].classList.add('active2');
 }
 else{reveals[i].classList.remove('active2');
 }
 }
 }



window.addEventListener("scroll", () => {
    const downPage = document.querySelector(".container");
    const triggerPoint = window.innerHeight / 6;

    if (window.scrollY > triggerPoint) {
        downPage.classList.add("active");
    } else {
        downPage.classList.remove("active");
    }
});


const textElements = document.querySelectorAll(".hero");


window.addEventListener("scroll", () => {
    const scrollPosition = window.scrollY;
    const triggerPoint = window.innerHeight / 10; 

   
    if (scrollPosition > triggerPoint) {
        document.body.style.backgroundImage = "url('static/dublicate.png')"; 
    } else {
        document.body.style.backgroundImage = "url('static/Screenshot 2024-11-06 135358.png')"; 
    }

    
    textElements.forEach((hero) => {
        
        const scaleValue = Math.max(0.5, 1 - scrollPosition / (2 * window.innerHeight));  disappear
        const opacityValue = Math.max(0, 1 - scrollPosition / (1.5 * window.innerHeight)); 
        text.style.transform = `scale(${scaleValue})`;
        text.style.opacity = opacityValue;
    });
});

window.addEventListener("scroll", function () {
    const revealElement = document.querySelector(".reveal2");
    const scrollTop = window.scrollY;
    
   
    if (scrollTop > 100) { 
        revealElement.classList.add("active2"); 
    } else {
        revealElement.classList.remove("active2");
    }
});













   
        