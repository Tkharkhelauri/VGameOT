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
