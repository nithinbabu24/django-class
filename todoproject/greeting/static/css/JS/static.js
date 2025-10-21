document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById("greetBtn");
    if (button) {
        button.addEventListener("click", function() {
            alert("Hello there! Welcome to my Django page!");
        });
    }
});
