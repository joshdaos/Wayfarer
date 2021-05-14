// Home Page Carousel JS
const carousels = bulmaCarousel.attach('.carousel', options);

for(let i = 0; i < carousels.length; i++) {
	carousels[i].on('before:show', state => {
		console.log(state);
        const element = document.querySelector('#my-element');
    });
}
if (element && element.bulmaCarousel) {
	element.bulmaCarousel.on('before-show', function(state) {
		console.log(state);
	});
}

// another option?
const carousels = bulmaCarousel.attach('.carousel', options);

const element = document.querySelector('#my-element');
if (element && element.bulmaCarousel) {
}