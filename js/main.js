window.addEventListener('load', function() {
    const photo1 = document.getElementById("photo1");
    console.log(photo1);
 
    photo1.addEventListener('click', () => {
        photo1.lastElementChild.classList.toggle('hidden');
    });
 
    const photo2 = document.getElementById("photo2");
    console.log(photo2);
 
    photo2.addEventListener('click', () => {
        photo2.lastElementChild.classList.toggle('hidden');
    });
 
    const photo3 = document.getElementById("photo3");
    console.log(photo3);
 
    photo3.addEventListener('click', () => {
        photo3.lastElementChild.classList.toggle('hidden');
    });
 
    const photo4 = document.getElementById("photo4");
    console.log(photo4);
 
    photo4.addEventListener('click', () => {
        photo4.lastElementChild.classList.toggle('hidden');
    });
 
    const photo5 = document.getElementById("photo5");
    console.log(photo5);
 
    photo5.addEventListener('click', () => {
        photo5.lastElementChild.classList.toggle('hidden');
    });
 });

 function scrollToMemory() {
    var memorySection = document.getElementById('Memory');
    if (memorySection) {
        memorySection.scrollIntoView({ behavior: 'smooth' });
    }
}