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
	$('#cd2').countdown({
		 until: runTimer,
		 onExpiry: EndCountdown,
		 onTick: Callbacks,
		 layout: '{mnn} {snn}'
	});

	function Callbacks(periods) {
		 if ($.countdown.periodsToSeconds(periods) === halfTime) {
				$('#cd2').addClass('halfway');
		 }
		 else if ($.countdown.periodsToSeconds(periods) <= 0) {
				EndCountdown();
		 }
	}

	function EndCountdown() {
		 $('#cd2').removeClass('halfway').addClass('ended');
		 $('#cd2').html('');
		 $('#gift2').hide();
		 $('#sale').prop('checked', false);
		 $('.input__sale').each(function(i, e) {
			e.checked = false
				$(e).prop('checked', false);
				$(e).attr('checked', false);
			$(e).remove()
		});
	}

});