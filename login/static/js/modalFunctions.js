function openModal(orderId) {
    console.log(`Attempting to open modal for order ID: ${orderId}`);
    const modal = document.getElementById(`modal-${orderId}`);
    if (modal) {
        modal.style.display = 'flex';
    } else {
        console.error(`Modal with ID modal-${orderId} not found.`);
    }
}

function closeModal(orderId) {
    console.log(`Attempting to close modal for order ID: ${orderId}`);
    const modal = document.getElementById(`modal-${orderId}`);
    if (modal) {
        modal.style.display = 'none';
    } else {
        console.error(`Modal with ID modal-${orderId} not found.`);
    }
}

// Add event listener for modal backdrop to close modal when clicked outside
document.querySelectorAll('.modal-backdrop').forEach(modal => {
    modal.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});

function trocarTexto(sobre) {
    // Seleciona o elemento pelo ID
    var elemento = document.getElementById('trocarTexto');

    // Verifica se estamos passando o mouse sobre o elemento
    if (sobre) {
        // Armazena o texto original apenas uma vez
        if (textoOriginal === "") {
            textoOriginal = elemento.innerHTML;
        }
        // Troca o texto para o novo texto
        elemento.innerHTML = "ID PRATO";
        elemento.classList.add('highlighted'); // Adiciona a classe de destaque
    } else {
        // Se não estiver mais sobre o elemento, restaura o texto original
        elemento.innerHTML = textoOriginal;
        elemento.classList.remove('highlighted'); // Remove a classe de destaque
    }
}
