function openNav() {
    document.getElementById('sideNav').style.width = "320px";
}
function closeNav() {
    document.getElementById('sideNav').style.width = "0";
}

// Skills event handlers
let skillExperience = document.getElementById('experience')
let skillLearning = document.getElementById('learning')
let experienceBox = document.querySelector('.boxSkill');
let learningBox = document.querySelector('.hidden');

skillLearning.addEventListener('click', () => {
    experienceBox.classList.add('hidden');
    experienceBox.classList.remove('boxSkill');
    learningBox.classList.add('boxSkill');

    // Activate the clicked button
    skillExperience.classList.remove('active');
    skillLearning.classList.add('active')
});

skillExperience.addEventListener('click', () => {
    experienceBox.classList.remove('hidden');
    experienceBox.classList.add('boxSkill');
    learningBox.classList.remove('boxSkill');

    // Activate the clicked button
    skillExperience.classList.add('active');
    skillLearning.classList.remove('active')
})

// ---------------Slider-----------------//

const slides = document.querySelectorAll('.slide');
const btnLeft = document.querySelector('.slider__btn--left');
const btnRight = document.querySelector('.slider__btn--right');
const dotContainer = document.querySelector('.dots');

let curSlide = 0;
const maxSlide = slides.length - 1;

// Creating dots
const createDots = function () {
    slides.forEach(function (_, i) {
      dotContainer.insertAdjacentHTML(
        'beforeend',
        `<button class="dots__dot" data-slide="${i}" aria-label="button"></button>`
      );
    });
};

createDots()

const activateDot = function (slide) {
document
    .querySelectorAll('.dots__dot')
    .forEach(dot => dot.classList.remove('dots__dot--active'));

document
    .querySelector(`.dots__dot[data-slide="${slide}"]`)
    .classList.add('dots__dot--active');
};
activateDot(0)

// Go to Slide 
const goToSlide = function(slide) {
    slides.forEach(
        (s, i) => (s.style.transform = `translateX(${100 * (i - slide)}%)`)
    );
}
goToSlide(0)

// Go to next slide right
const rightSlide = function () {
    if(curSlide === maxSlide) {
        curSlide = 0;
    }else {
        curSlide++;
    }
    goToSlide(curSlide)
    activateDot(curSlide)
}
// Go to next slide left
const leftSlide = function() {
    if(curSlide === 0){
        curSlide = maxSlide;
    }else {
        curSlide--
    }
    goToSlide(curSlide)
    activateDot(curSlide)
}

// Next slide 
btnRight.addEventListener('click', rightSlide)
btnLeft.addEventListener('click', leftSlide)

// Handlling Arrow key to move the slides
document.addEventListener('keydown', function(e) {
    if(e.key === 'ArrowRight') rightSlide() 
})

// Dot event handling
dotContainer.addEventListener('click', function (e) {
    if (e.target.classList.contains('dots__dot')) {
        const { slide } = e.target.dataset;
        goToSlide(slide);
        activateDot(slide);
    }
});
