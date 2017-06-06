$(function(){
	$(document).ajaxStart(function(){
		$('.title img').show();
	});
	$(document).ajaxStop(function(){
		$('.title img').hide();
	});
	
    $('.sbutton').on('click',function(){
	    $.get('netlist',{
		    inet: $('.inet').val()
	    }, function(data){
		    $('.iplist ul').html(data);
	});
    });
	
	$('.iplist ul').on('click','li.toscan',function(){
		$.get('gethostname',{
			host: $(this).text()
		}, function(data){
			$('.hostname').text(data);
		});
		$('.ipname').text($(this).text())
		$('.ipscan').show();
		$('.dashboard').hide();
	});
});
