$(function() {
	var $navigation = $('#navigation');
	var nav_offset_y = $navigation.offset().top;

	function fixedNavigation() {
		if ($(window).scrollTop() > nav_offset_y) {
			$navigation.css({
				'top': 0,
				'position': 'fixed'
			});
		} else {
			$navigation.css({
				'top': nav_offset_y + 'px',
				'position': 'absolute'
			});
		}
	}

	$(window).scroll(fixedNavigation);
});