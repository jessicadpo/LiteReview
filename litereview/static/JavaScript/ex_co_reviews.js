// Portions of this code have been provided by https://www.w3schools.com/howto/howto_js_collapsible.asp

var btn = document.getElementsByClassName("expand-button");
var review = document.getElementsByClassName("expanded-review");
var i;

for (i = 0; i < btn.length; i++) {
  let j = i;
  btn[i].addEventListener("click", function() {
    this.classList.toggle("active");
    if (review[j].style.display === "block"){
      review[j].style.display = "none";
    } else {
      review[j].style.display = "block";
    }
  });
}