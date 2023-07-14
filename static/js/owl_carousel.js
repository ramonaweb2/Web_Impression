$(document).ready(function(){

    let owl = $('.owl-carousel');
    owl.owlCarousel({
        loop: true,
        nav: true,
        margin: 10,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            960:{
                items:3
            },
            1200:{
                items:4
            }
        }
    });
    owl.on('mousewheel', '.owl-stage', function (e) {
        if (e.deltaY > 0) {
            owl.trigger('next.owl');
        } else {
            owl.trigger('prev.owl');
        }
        e.preventDefault();
    });


});