# data-exploration

food website - slideshow


baseline goal:
3 pages
how each candidate did in their hometown
what state had most Democratic voters/ most Republican voters?
How many people votes "no preference"?

Ben Carson			 Detroit, Michigan					
Bernie Sanders		 Brooklyn, New York				
Carly Fiorina		 Austin, Texas						
Chris Christie		 Newark, New Jersey					
Donald Trump		 Queens, New York City				
Hillary Clinton		 Chicago, Illinois					
Jeb Bush			 Midland, Texas						
John Kasich			 McKees Rocks, Pennsylvania			
Marco Rubio			 Miami, Florida						
Martin O'Malley 	 Washington, D.C.					
Mike Huckabee		 Hope, Arkansas						
Rand Paul			 Pittsburgh, Pennsylvania			
Rick Santorum		 Winchester, Virginia				
Ted Cruz			 Houston, Texas						

gridColor: "rgba(1,77,101,.1)",
interlacedColor: "rgba(1,77,101,.2)",

 graphpoint+= Markup( '{ y: ' + str(votes[num]) + ', label: "' + str(num) + '",' + ' indexLabel: " ' + str(host[num]) + ' " },' )

 
 
<script>
window.onload = function () {

//Better to construct options first and then pass it as a parameter
var options = {
	animationEnabled: true,
	backgroundColor: "#E2EBEB",
	title: {
		text: "How well did each candidate do in their home state?",                
		fontColor: "Peru"
	},	
	axisY: {
		tickThickness: 0,
		lineThickness: 0,
		valueFormatString: " ",
		gridThickness: 0                    
	},
	axisX: {
		tickThickness: 0,
		lineThickness: 0,
		labelFontSize: 18,
		labelFontColor: "Peru"				
	},
	data: [{
		indexLabelFontSize: 15,
		toolTipContent: "<span style=\"color:#62C9C3\">{indexLabel}:</span> <span style=\"color:#CD853F\"><strong>{y}</strong></span>",
		indexLabelPlacement: "inside",
		indexLabelFontColor: "white",
		indexLabelFontWeight: 600,
		indexLabelFontFamily: "Verdana",
		color: "#62C9C3",
		type: "bar",
		dataPoints: [
			{{graphpoint}}
		]
	}]
};

$("#chartContainer").CanvasJSChart(options);
}
</script>