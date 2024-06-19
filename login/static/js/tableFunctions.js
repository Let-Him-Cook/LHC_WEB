document.addEventListener("DOMContentLoaded", function() {
    var pedidos = document.getElementsByClassName("pedido");

    Array.from(pedidos).forEach(function(pedido) {
        var header = pedido.querySelector(".pedido-header");
        var timeoutId;

        if (header) {  // Verifica se header não é nulo
            header.addEventListener("mouseenter", function(event) {
                var desc = pedido.querySelector(".desc");
                if (desc) {  // Verifica se desc não é nulo
                    clearTimeout(timeoutId);
                    desc.classList.add("show");
                }
            });

            pedido.addEventListener("mouseleave", function(event) {
                var desc = pedido.querySelector(".desc");
                if (desc) {  // Verifica se desc não é nulo
                    timeoutId = setTimeout(function() {
                        if (!pedido.contains(document.elementFromPoint(event.clientX, event.clientY))) {
                            desc.classList.remove("show");
                        }
                    }, 100);  // Ajuste o tempo conforme necessário
                }
            });

            pedido.addEventListener("mouseenter", function(event) {
                clearTimeout(timeoutId);
            });
        }
    });
});
