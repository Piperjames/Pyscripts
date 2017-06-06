$(function(){
	$(document).ajaxStart(function(){
		$('.title img').show();
	});
	$(document).ajaxStop(function(){
		$('.title img').hide();
	});
<<<<<<< HEAD
	
=======
<<<<<<< HEAD
	
=======
>>>>>>> f1ce60a788156a189832a523ebf723823a1bac8a
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67
    $('.sbutton').on('click',function(){
	    $.get('netlist',{
		    inet: $('.inet').val()
	    }, function(data){
		    $('.iplist ul').html(data);
	});
    });
<<<<<<< HEAD
	
	$('.iplist ul').on('click','li.toscan',function(){
=======
<<<<<<< HEAD
	
	$('li.toscan').on('click',function(){
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67
		$.get('gethostname',{
			host: $(this).text()
		}, function(data){
			$('.hostname').text(data);
		});
<<<<<<< HEAD
		$('.ipname').text($(this).text())
		$('.ipscan').show();
		$('.dashboard').hide();
	});
=======
		$('.dashboard').hide();
		$('.ipname').text($(this).text())
		$('.ipscan').show();
	});
=======
>>>>>>> f1ce60a788156a189832a523ebf723823a1bac8a
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67
});
