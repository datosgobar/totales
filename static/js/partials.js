$(function() {

	var total = $('#total').text();

	$('li').mouseenter(function() {
		$(this).addClass('highlight');
		var amount = $(this).find('#amount').text();
		var percentage = (amount / total * 100).toFixed(2);
		var item = $(this).find('#name').text();
		var info = item + ': ' + percentage + '% del total';
		$('.partial').html(info);
	});
	
	$('li').mouseleave(function() {
		$(this).removeClass('highlight');
		$('.partial').html('');
	});

})