var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("header").style.top = "0";
} else {
    document.getElementById("header").style.top = "-90px";
  }
  prevScrollpos = currentScrollPos;
}

window.addEventListener('scroll', function() {
    const target = document.querySelector('.main-bg');

    var scrolled = window.pageYOffset;
    var rate = scrolled * 0.1;

    target.style.top = '-'+rate+'px'
});

function openNav() {
    document.getElementById("sideNav").style.width = "250px";

  }
  
  function closeNav() {
    document.getElementById("sideNav").style.width = "0";

  }