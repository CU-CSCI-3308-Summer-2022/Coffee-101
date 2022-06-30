
const coffee = [
  {
    name: "Espresso",
    img: "../static/img/espresso.png",
    alt: "Image of Espresso",
    type: "Espresso (2oz)",
    cup_size: "3oz Cup",
    milk: "None",
    foam: "None",
  },
  {
    name: "Cappuccino",
    img: "../static/img/cappuccino.png",
    alt: "Image of Cappuccino",
    type: "Espresso (2oz)",
    cup_size: "8oz Cup",
    milk: "Steamed (2oz)",
    foam: "Milk Foam (2oz)",
  },
  {
    name: "Latte",
    img: "../static/img/latte.png",
    alt: "Image of Latte",
    type: "Espresso (2oz)",
    cup_size: "12oz Cup",
    milk: "Steamed (9oz)",
    foam: "Milk Foam (1oz)",
  },
  {
    name: "Macchiato",
    img: "../static/img/macchiato.png",
    alt: "Image of Macchiato",
    type: "Espresso (2oz)",
    cup_size: "3oz Cup",
    milk: "None",
    foam: "Milk Foam (1oz)",
  },
];



function loadCoffeePage() {
	for(var i = 0; i < coffee.length; i++){
		var x = document.createElement("a");
		x.setAttribute("href", "#");
		x.setAttribute("class", "dropdown-item");
		let count = i;
		x.onclick = function () { switchCoffee(count) } 
		var t = document.createTextNode(coffee[i].name);
		x.appendChild(t);
		document.getElementById('coffee_selector').appendChild(x);
	}
}

function switchCoffee(coffeeNum) {1
  document.getElementById('coffee_img').src= coffee[coffeeNum].img;
  document.getElementById('coffee_img').alt= coffee[coffeeNum].alt;
	document.getElementById('c_type').innerHTML = coffee[coffeeNum].type;
	document.getElementById('c_cup').innerHTML = coffee[coffeeNum].cup_size;
	document.getElementById('c_milk').innerHTML = coffee[coffeeNum].milk;
	document.getElementById('c_foam').innerHTML= coffee[coffeeNum].foam;

}