const profileIcon = document.getElementById("profileIcon");
const profileDropdown = document.getElementById("profileDropdown");

profileIcon.addEventListener("click", () => {
  profileDropdown.style.display = profileDropdown.style.display === "block" ? "none" : "block";
});

// Close dropdown when clicking outside of it
window.onclick = function(event) {
  if (!event.target.matches('#profileIcon')) {
    if (profileDropdown.style.display === "block") {
      profileDropdown.style.display = "none";
    }
  }
}


const hamburgerButton = document.querySelector('.hamburger button');
const navMenu = document.querySelector('.nav-menu');

hamburgerButton.addEventListener('click', () => {
    navMenu.classList.toggle('visible');
    hamburgerButton.setAttribute('aria-expanded', navMenu.classList.contains('visible'));
});