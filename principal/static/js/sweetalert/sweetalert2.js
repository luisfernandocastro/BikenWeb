Swal.fire({
	html: 'Por favor acepte nuestros <a href="#">terminos y condiciones</a>',
	icon: 'info',
	confirmButtonText: 'Acepto',
	padding: '1rem',
	backdrop: true,
	toast: true,
	position: 'bottom-start',
	allowOutsideClick: false,
	allowEscapeKey: false,
	stopKeydownPropagation: false,


	showConfirmButton: true,
	confirmButtonColor: '#2059BD',
	//confirmButtonAriaLabel: 

	customClass:{
		content: 'content-class'
	}
	
});
