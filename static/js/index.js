$(window).scroll(function (){
  $('nav').toggleClass('scrolled',$(this).scrollTop() > 100);
});



function myFunction() {
  alert("Change Made");
}