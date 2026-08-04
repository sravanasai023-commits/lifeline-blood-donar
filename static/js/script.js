// LifeLink JavaScript

document.addEventListener("DOMContentLoaded", function () {

    console.log("LifeLink Loaded Successfully!");

    // Auto-hide flash messages
    const flash = document.querySelector(".flash");

    if (flash) {
        setTimeout(() => {
            flash.style.display = "none";
        }, 3000);
    }

});