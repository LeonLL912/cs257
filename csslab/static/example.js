
the_heading = document.getElementById("hello");
const color = the_heading.style.color;

the_heading.onclick = function(){ the_heading.innerText="Goodbye World!"};

the_paragraph = document.getElementById("paragraph1");

var counter = 1;
function changeColor() {
  if (counter % 2 == 1){
  	text_input_element = document.getElementById("user-color");
  	new_color = text_input_element.value;
		the_heading.style.color = new_color;
  	button.innerText="OMG, this is even worse! Change The Color Back";
    counter++;
  }
  else{
		the_heading.style.color = color;
  	button.innerText="Change Color"; 
    counter++;
  }
  
}