(function () {
  const btnEliminacion = document.querySelectorAll('.btnEliminacion');
  btnEliminacion.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const confirmacion = confirm('Seguro de eliminar el registro?');
      if (!confirmacion) {
        e.preventDefault();
      }
    });
  });

  $(document).ready(function () {
    // Oculta la alerta después de 3 segundos
    setTimeout(function () {
      $('.alert').alert('close');
    }, 3000);
  });
})();
