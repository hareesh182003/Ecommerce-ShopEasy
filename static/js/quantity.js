function updateQuantity(action, productId) {
        const quantityElement = document.getElementById(`quantity-value-${productId}`);
        let currentQuantity = parseInt(quantityElement.textContent, 10);

        if (action === 'inc') {
            currentQuantity += 1;
        } else if (action === 'dec' && currentQuantity > 1) {
            currentQuantity -= 1;
        }

        quantityElement.textContent = currentQuantity;

    }