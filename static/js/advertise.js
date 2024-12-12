const carousel = document.querySelector('.carousel');

        function duplicateCarouselItems() {
            const items = carousel.innerHTML; // Get the initial items
            carousel.innerHTML += items;     // Duplicate them
        }

        duplicateCarouselItems(); // Call once on page load

