document.addEventListener('DOMContentLoaded', function() {
    // Mostrar el carrito al cargar la página
    mostrarCarrito();

    // Función para mostrar el carrito
    function mostrarCarrito() {
        const listaCarrito = document.getElementById('lista-carrito');
        const totalCarrito = document.getElementById('total-carrito');
        let total = 0;

        // Limpiar el contenido previo del carrito
        listaCarrito.innerHTML = '';

        // Obtener el carrito del localStorage
        const carrito = JSON.parse(localStorage.getItem('carrito')) || [];

        // Mostrar cada elemento del carrito
        carrito.forEach((item, index) => {
            const li = document.createElement('li');
            li.textContent = `${item.nombre} - Precio: $${item.precio}`;

            // Botón para quitar el elemento del carrito
            const btnQuitar = document.createElement('button');
            btnQuitar.textContent = 'Quitar';
            btnQuitar.addEventListener('click', () => {
                // Al hacer clic en el botón, eliminar el elemento del carrito y actualizar la vista
                carrito.splice(index, 1);
                localStorage.setItem('carrito', JSON.stringify(carrito));
                mostrarCarrito(); // Mostrar el carrito actualizado
            });

            li.appendChild(btnQuitar);
            listaCarrito.appendChild(li);
            total += item.precio;
        });

        // Mostrar el total del carrito
        totalCarrito.textContent = total;

        // Verificar si el carrito está vacío
        if (carrito.length === 0) {
            // Si está vacío, mostrar mensaje de color rojo
            const mensajeCarritoVacio = document.createElement('p');
            mensajeCarritoVacio.textContent = 'No hay elementos en el carrito';
            mensajeCarritoVacio.style.color = 'red';
            listaCarrito.appendChild(mensajeCarritoVacio);
        }
    }

    // Agregar evento al botón de comprar
    const btnComprar = document.getElementById('btn-comprar');
    btnComprar.addEventListener('click', () => {
        // Verificar si ya existe un mensaje de compra
        const mensajeCompraExistente = document.getElementById('mensaje-compra');
        if (!mensajeCompraExistente) {
            // Si no existe, mostrar el mensaje de compra
            const mensajeCompra = document.createElement('p');
            mensajeCompra.textContent = '¡Compra realizada con éxito!';
            mensajeCompra.style.color = 'green';
            mensajeCompra.id = 'mensaje-compra';
            btnComprar.parentNode.appendChild(mensajeCompra); // Agregar mensaje debajo del botón
            // Aquí podrías agregar el código para realizar la compra
        }
    });
});
