$(window).load(function(){

    var $container = $('.partnersLogos');
        masonry: {
            columnWidth: 165;
            gutter:10
        }
    $container.isotope({
        filter: '*',
        animationOptions: {
            duration: 750,
            easing: 'linear',
            queue: false
        },
    });

    $('.partnersLogosFilter button').click(function(){
        $('.partnersLogosFilter .current').removeClass('current');
        $(this).addClass('current');

        var selector = $(this).attr('data-filter');
        $container.isotope({
            filter: selector,
            animationOptions: {
                duration: 750,
                easing: 'linear',
                queue: false
            }
         });
         return false;
    });
});