window.onload = function() {
    var img = document.getElementById('profile');
    
    img.classList.add('fade-in-visible');
  };
window.addEventListener('load', function() {
    const aboutSection = document.getElementById('about');
    
    setTimeout(function() {
        aboutSection.classList.add('fly-up');
    }, 500); 
})