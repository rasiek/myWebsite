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

const words = ["Développement Backend", "Développement Logiciel", "Création de Produit", "Développement Arduino", "Création Multimédia"] 

const Typewriter = function(txtElement, words) {

  this.txtElement = txtElement
  this.words = words
  this.txt = ''
  this.wordIndex = 0
  this.type()
  this.switch = false
  this.isDeleting = false

}

Typewriter.prototype.type = function() {

  const currentWord = this.wordIndex % this.words.length
  const fullTxt = this.words[currentWord]
  const cursor = document.getElementById("t-cursor")

  if(this.isDeleting) {
    
    this.txt = fullTxt.substring(0, this.txt.length -1)

    if (this.txt.length <= 0) {
      cursor.classList.add("blink")
      if (this.switch) {
        setTimeout(() => {
          this.isDeleting = false
          this.wordIndex = this.wordIndex + 1
          cursor.classList.remove("blink")
        }, 2000)

        this.switch = false
      }

    }


  } else {

    this.txt = fullTxt.substring(0, this.txt.length + 1)

    if (this.txt.length == fullTxt.length) {
      
      cursor.classList.add("blink")
      setTimeout(() => { 
        this.isDeleting = true
        cursor.classList.remove("blink")
        this.switch = true
      }, 2000)
    }
    
  }

  this.txtElement.innerHTML = this.txt
  setTimeout(() => this.type(), 200)
}

const init = () => {
    const txtElement = document.getElementById("typewriter")

    new Typewriter(txtElement, words)

}

if (document.location.pathname == "/") {

  document.addEventListener('DOMContentLoaded', init)

}

