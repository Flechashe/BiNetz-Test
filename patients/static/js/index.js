(function () {

    const deleteBtn = document.querySelectorAll('.delete-btn');

    deleteBtn.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            const confirmation = confirm(
                '¿Seguro de eliminar el registro del paciente?'
            );
            if (!confirmation) {
                e.preventDefault();
            }
        });
    });

})();
