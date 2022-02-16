console.log("Spartacus")

btn = document.getElementById('lsBtn');
btn.addEventListener("click", turnUpFunction);

nbDeg=180;
function turnUpFunction(){
	btn.style.transform='rotate('+nbDeg+'deg)';
	nbDeg = nbDeg == 180 ? 0 : 180;
}

imgOn = document.getElementsByClassName('imgOn');
imgOff = document.getElementsByClassName('imgOff');



