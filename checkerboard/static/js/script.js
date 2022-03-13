$(document).ready(function() {
	var pathname = window.location.pathname;
	pathParts = pathname.split('/');
	if (pathParts.length > 3) {
		var c1 = pathParts[3];
		var c2 = pathParts[4];
		$('.color1').css('background-color', c1);
		$('.color2').css('background-color', c2);
	}
});