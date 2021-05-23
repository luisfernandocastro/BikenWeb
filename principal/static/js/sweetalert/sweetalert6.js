Swal.fire({
	title: '<span class="alerttit">Registro Exitoso</span>',
	text: 'Inicia  para poder continuar',
	// html:
	icon: 'success',
	confirmButtonText: 'Ok',
	footer: '<span class="alerttit2">Gracias por unirte a nuestra comunidad Biken.</br> Ahora puedes subir y administrar tu Bicicleta</span>',
	//width: '50%',
	padding: '2rem',
	// background:
	// grow:
	backdrop: true,
	// timer:
	// timerProgressBar:
	// toast:
	position: 'center',
	allowOutsideClick: false,
	allowEscapeKey: false,
	allowEnterKey: false,
	stopKeydownPropagation: false,

	// input:
	// inputPlaceholder:
	// inputValue:
	// inputOptions:

	//  customClass:
	// 	container:
	// 	popup:
	// 	header:
	// 	title:
	// 	closeButton:
	// 	icon:
	// 	image:
	// 	content:
	// 	input:
	// 	actions:
	// 	confirmButton:
	// 	cancelButton:
	// 	footer:	

	showConfirmButton: true,
	confirmButtonColor: '#2059BD',
	//confirmButtonAriaLabel: 

	// showCancelButton:
	// cancelButtonText:
	// cancelButtonColor:
	// cancelButtonAriaLabel:

	//buttonsStyling: true,
	//showCloseButton: true,
	//closeButtonAriaLabel: 'cerrar alerta',


	// imageUrl:
	// imageWidth:
	// imageHeight:
	// imageAlt:

}).then((result) => {
	if (result.value) {
		window.location.href = '../../../templates/pages/comunidad.html'
	}
});
