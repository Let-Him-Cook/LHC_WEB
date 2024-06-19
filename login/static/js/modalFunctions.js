// Função para abrir o modal
function openModal() {
    document.getElementById('modalBackdrop').style.display = 'flex';
}

// Função para fechar o modal
function closeModal() {
    document.getElementById('modalBackdrop').style.display = 'none';
}

var textoOriginal = "";

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
