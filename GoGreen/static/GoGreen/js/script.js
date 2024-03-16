window.addEventListener('scroll', function () {
    localStorage.setItem('scrollPosition', window.scrollY);
});
document.addEventListener('DOMContentLoaded', async function () {
    // Save scroll state in local storage
    
    var scrollPosition = localStorage.getItem('scrollPosition', 0);
    if (scrollPosition) {
        window.scrollTo({
            top: scrollPosition,
            behavior: 'smooth'
        });
    }
  });
  