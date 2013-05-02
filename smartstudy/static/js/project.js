function initialize() {
  var mapOptions = {
    zoom: 8,
    center: new google.maps.LatLng(-34.397, 150.644),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  var map = new google.maps.Map(document.getElementById('map'),
      mapOptions);
}

function loadScript() {
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&' +
      'callback=initialize';
  document.body.appendChild(script);
}


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
	$(window).on('load', loadScript);
});