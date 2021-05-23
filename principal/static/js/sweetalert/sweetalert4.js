Swal.fire({
	title: '<span class="alerttit">Excelente</span>',
	text: 'Subiste tu bicicleta Exitosamente',
	// html:
	icon: 'success',
	confirmButtonText: 'Ok',
	footer: 'Gracias por unirte a nuestra comunidad Biken.',
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
  		window.location.href = '../pages/estadisticasComunidad.html'
	}
		});
