function validateLoginForm() {
    var email = $('#loginEmail').val();
    var password = $('#loginPassword').val();
    var isValid = true;

    // Validación del correo electrónico
    if (email.trim() === '') {
        $('#mensajeLoginEmail').text('Por favor, introduce tu correo electrónico').addClass('text-danger');
        isValid = false;
    } else {
        $('#mensajeLoginEmail').text('').removeClass('text-danger');
    }

    // Validación de la contraseña
    if (password.trim() === '') {
        $('#mensajeLoginPassword').text('Por favor, introduce tu contraseña').addClass('text-danger');
        isValid = false;
    } else {
        $('#mensajeLoginPassword').text('').removeClass('text-danger');
    }

    return isValid;
}

function validateRegisterForm() {
    var username = $('#registerUsername').val();
    var email = $('#registerEmail').val();
    var password = $('#registerPassword').val();
    var captcha = $('#captcha').val();
    var isValid = true;

    // Validación del nombre de usuario
    if (username.trim() === '') {
        $('#mensajeRegisterUsername').text('Por favor, introduce un nombre de usuario').addClass('text-danger');
        isValid = false;
    } else {
        $('#mensajeRegisterUsername').text('').removeClass('text-danger');
    }

    // Validación del correo electrónico
    if (email.trim() === '') {
        $('#mensajeRegisterEmail').text('Por favor, introduce tu correo electrónico').addClass('text-danger');
        isValid = false;
    } else if (!isValidEmail(email)) {
        $('#mensajeRegisterEmail').text('Por favor, introduce un correo electrónico válido').addClass('text-danger');
        isValid = false;
    } else {
        $('#mensajeRegisterEmail').text('').removeClass('text-danger');
    }

    // Validación de la contraseña
    if (password.trim() === '') {
        $('#mensajeRegisterPassword').text('Por favor, introduce tu contraseña').addClass('text-danger');
        isValid = false;
    } else {
        $('#mensajeRegisterPassword').text('').removeClass('text-danger');
    }

    // Validación del captcha
    if (captcha.trim() !== '12') {
        $('#mensajeCaptcha').text('La respuesta al captcha es incorrecta').addClass('text-danger');
        isValid = false;
    } else {
        $('#mensajeCaptcha').text('').removeClass('text-danger');
    }

    return isValid;
}

function isValidEmail(email) {
    // Expresión regular para verificar el formato del correo electrónico
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        if (!validateLoginForm()) {
            event.preventDefault(); // Evita que se envíe el formulario si la validación falla
        }
    });

    $('#registerForm').submit(function(event) {
        if (!validateRegisterForm()) {
            event.preventDefault(); // Evita que se envíe el formulario si la validación falla
        }
    });

    $('#loginForm input').on('input', function() {
        validateLoginForm();
    });

    $('#registerForm input').on('input', function() {
        validateRegisterForm();
    });
});
