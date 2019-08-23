$(".hamburger").click(function(e) {
	e.preventDefault();
	$(this).toggleClass('is-active');
	$(".menu__hamb").toggleClass('mhback shadow');
	$(".navs").toggleClass('hiddens');
	
})

