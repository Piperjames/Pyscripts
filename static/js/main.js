$(function(){
	$(document).ajaxStart(function(){
		$('.title img').show();
	});
	$(document).ajaxStop(function(){
		$('.title img').hide();
	});
<<<<<<< HEAD
	
=======
>>>>>>> f1ce60a788156a189832a523ebf723823a1bac8a
    $('.sbutton').on('click',function(){
	    $.get('netlist',{
		    inet: $('.inet').val()
	    }, function(data){
		    $('.iplist ul').html(data);
	});
    });
<<<<<<< HEAD
	
	$('li.toscan').on('click',function(){
		$.get('gethostname',{
			host: $(this).text()
		}, function(data){
			$('.hostname').text(data);
		});
		$('.dashboard').hide();
		$('.ipname').text($(this).text())
		$('.ipscan').show();
	});
=======
>>>>>>> f1ce60a788156a189832a523ebf723823a1bac8a
});
