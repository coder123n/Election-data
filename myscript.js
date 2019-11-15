$(document).ready(function(){
	$("#ans1").hide();
	$("#ans2").hide();
	$("#ans3").hide();
	$("#q1").click(function(){
		$("#ans1").toggle();
	});
	$("#q2").click(function(){
		$("#ans2").toggle();
	});
	$("#q3").click(function(){
		$("#ans3").toggle();
	});

});
