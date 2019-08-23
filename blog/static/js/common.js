$(function() {

	// Custom JS

	$('.title__slide').slick({
		centerMode: true,
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: false,
		dots: true,
		fade: true,
		autoplay: true,
		pauseOnHover: false,
		pauseOnFocus: false,
		autoplaySpeed: 4000
	});

	$('.m-slider').slick({
	    arrows: false,
		dots: true,
		autoplay: true,
	});

});