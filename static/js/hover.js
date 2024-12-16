document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector(".filters-toggle");
    const filtersSection = document.querySelector(".filters-section");

    toggleButton.addEventListener("click", function () {
        if (filtersSection.style.display === "block") {
            filtersSection.style.display = "none";
        } else {
            filtersSection.style.display = "block";
        }
    });
});