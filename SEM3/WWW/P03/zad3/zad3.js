var i = 0;
var boxes = ["box1", "box2","box3","box4","box5"];

function move(){
	intervalId=setInterval(function(){moveUp(boxes[i]); }, 200);
}

function moveUp(box){
	if(i == 5){
		clearInterval(intervalId);
		i = 0;
		intervalId1=setInterval(function(){moveDown(boxes[i]); }, 200);
	}
	else{
		document.getElementById(box).style.bottom="-80px";
		i++;
	}
}

function moveDown(box){
	if(i == 5){
		clearInterval(intervalId1);
		i = 0;
		intervalId=setInterval(function(){moveUp(boxes[i]); }, 200);
	}
	else{
		document.getElementById(box).style.bottom="-140px";
		i++;
	}
}