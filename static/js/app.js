const body = document.querySelector("#body");
const hamBurger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamBurger.addEventListener("click", () => {
    hamBurger.classList.toggle("visible");
    navMenu.classList.toggle("visible");
    body.classList.toggle("shadow");
document.querySelectorAll(".nav-link").forEach(n => n.
addEventListener("click", () => {
    hamBurger.classList.remove("visible");
    navMenu.classList.remove("visible");
    }))
})