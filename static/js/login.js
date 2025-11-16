document.getElementById('loginForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const inputs = this.querySelectorAll('input');
  const message = document.getElementById('message');
  let isValid = true;

  inputs.forEach(input => {
    if (input.value.trim() === '') {
      message.textContent = 'Todos os campos são obrigatórios.';
      isValid = false;
    }
  });

  const email = document.querySelector('input[name="email"]').value.trim();
  const password = document.querySelector('input[name="password"]').value;

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    message.textContent = 'Email inválido. Use o formato exemplo@dominio.com.';
    isValid = false;
  }

  if (password.length < 8) {
    message.textContent = 'A senha deve ter no mínimo 8 caracteres.';
    isValid = false;
  }

  if (isValid) {
    this.submit();
  }
});
