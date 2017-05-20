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
});
