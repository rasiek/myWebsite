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
  

  // Typewriting func

const words = ["Création Multimedia", "Création de Produit", "Dévelopement Backend", "Dévelopement Logiciel", "Arduino"] 

const Typewriter = function(txtElement, words) {

  this.txtElement = txtElement
  this.words = words
  this.txt = ''
  this.wordIndex = 0
  this.wait = 3000
  this.type()
  this.isDeleting = false

}

Typewriter.prototype.type = function() {

  const currentWord = this.wordIndex % this.words.length
  const fullTxt = this.words[currentWord]
  console.log(fullTxt)

  if(this.isDeleting) {
    
    this.txt = fullTxt.substring(0, this.txt.length -1)

    if (this.txt.length == 0) {
      this.isDeleting = false    
      this.wordIndex = this.wordIndex + 1
    }


  } else {

    this.txt = fullTxt.substring(0, this.txt.length + 1)

    if (this.txt.length == fullTxt.length) {
      setTimeout(() => { this.isDeleting = true}, 2000)
    }
    
  }
  console.log(currentWord)

  this.txtElement.innerHTML = this.txt
  setTimeout(() => this.type(), 200)
}

const init = () => {
    const txtElement = document.getElementById("typewriter")
    console.log(txtElement)

    new Typewriter(txtElement, words)

}

if (document.location.pathname == "/") {

  document.addEventListener('DOMContentLoaded', init)

}

