
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (document.body.scrollTop > 90 || document.documentElement.scrollTop > 90) {
    document.getElementById("navbar").style.padding = "20px 10px";
  }
else {
    document.getElementById("navbar").style.padding = "50px 10px";
  }
}
