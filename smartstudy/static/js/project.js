$(function () {
    var $navbar = $('.navbar');
    var navbar_offset_y = $navbar.offset().top;

    function fixedNavigation() {
        if ($(window).scrollTop() > navbar_offset_y) {
            $navbar.css({
                'position': 'fixed',
                'top': 0
            });
        } else {
            $navbar.css({
                'position': 'relative'
            });
        }
    }

    $(window).scroll(fixedNavigation);
    $navbar.scrollspy();
});
