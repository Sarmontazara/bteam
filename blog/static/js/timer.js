$(document).ready(function() {

	var totalTime = 300; // Amout of time (sec)
	var halfTime = Math.floor(totalTime / 2);

	if (!Cookies.get('cdTime')) {
		 var now = $.now(); // First time on page
		 Cookies.set('firstTime', now, {
				expires: 7,
				path: '/'
		 });
		 Cookies.set('cdTime', totalTime, {
				expires: 7,
				path: '/'
		 });
		 var runTimer = Cookies.get('cdTime');
	} else {
		 var currentTime = $.now();
		 var usedTime = (currentTime - Cookies.get('firstTime')) / 1000; // Calculate and convert into seconds
		 var runTimer = Cookies.get('cdTime') - usedTime;
	}
	$('#cd').countdown({
		until: runTimer,
		onExpiry: EndCountdown,
		onTick: Callbacks,
		layout: '{mnn} {snn}',
	});

	function Callbacks(periods) {
		 if ($.countdown.periodsToSeconds(periods) === halfTime) {
				$('#cd').addClass('halfway');
		 }
		 else if ($.countdown.periodsToSeconds(periods) <= 0) {
				EndCountdown();
		 }
	}

	function EndCountdown() {
		$('#cd').removeClass('halfway').addClass('ended');
		$('#cd').html('');		 
		$('#gift').removeClass('visible').addClass('hidden');
		$('#colum').removeClass('col-12 col-lg-6').addClass('col-12 mx-auto center');
		$('#gift__form').addClass('hidden');
		$('#gift__form__without').removeClass('hidden').addClass('visible');
		$('.btn__fix').removeClass('hiddens').addClass('visible');
		$('.input__sale').each(function(i, e) {
			e.checked = false
				$(e).prop('checked', false);
				$(e).attr('checked', false);
			$(e).remove()

		});
	}

});