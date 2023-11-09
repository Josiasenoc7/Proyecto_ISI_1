const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const bthPopup = document.querySelector('.bthLogin-popup');
const iconClose = document.querySelector('.icon-close');
const buyButtons = document.querySelectorAll('.buy-button');

registerLink.addEventListener('click', () => wrapper.classList.add('active'));
loginLink.addEventListener('click', () => wrapper.classList.remove('active'));
bthPopup.addEventListener('click', () => wrapper.classList.add('active-popup'));
iconClose.addEventListener('click', () => wrapper.classList.remove('active-popup'));

buyButtons.forEach(button => {
    button.addEventListener('click', () => {
        alert('¡Gracias por tu compra!');
    });
});