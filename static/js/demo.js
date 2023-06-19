$(document).ready(function(){
  $(".owl-carousel").owlCarousel({
    center: true,
    items: 2,
    loop: true,
    nav: true,
    margin: 30,
    responsive: {
        992:{
            items:4
        }
    }
  });
});