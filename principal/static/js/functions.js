
$(window).on('load', function () {
	setTimeout(function () {
		$(".loader-page").css({ visibility: "hidden", opacity: "0" })
	}, 2000);
});


/////todos los inputs
$(document).ready(function () {
	$("input").focus(function () {
		$(this).css("background-color", "#F1F5FC");
	});
	$("input").blur(function () {
		$(this).css("background-color", "white");
	});
}); html:




$("#alert,#alert3,#alert5,#alert7,#alert9,#alert11").click(function () {
	Swal.fire({
		title: '<span class="alerttit">No estas registrado</span>',
		text: 'Registrate para continuar con el alquiler',
		//
		// background:
		// grow:
		//backdrop: false,
		// timer:
		// timerProgressBar:
		// toast:
		// position:
		// allowOutsideClick:
		// allowEscapeKey:
		// allowEnterKey:
		// stopKeydownPropagation:

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

		buttonsStyling: true,
		showCloseButton: true,
		closeButtonAriaLabel: 'cerrar alerta',


		// imageUrl:
		// imageWidth:
		// imageHeight:
		// imageAlt:

	}).then((result) => {
		if (result.value) {
			window.location.href = "{% url 'pages/inicio' %}"
		}
	});
});


$("#alert2,#alert4,#alert6,#alert8,#alert10,#alert12").click(function () {
	Swal.fire({
		title: '<span class="alerttit">No estas registrado</span>',
		text: 'Registrate para poder añadir al carrito',
		// html:
		icon: 'info',
		confirmButtonText: 'Registrarse',
		// footer:
		// width:
		padding: '2rem',
		// background:
		// grow:
		//backdrop: false,
		// timer:
		// timerProgressBar:
		// toast:
		// position:
		// allowOutsideClick:
		// allowEscapeKey:
		// allowEnterKey:
		// stopKeydownPropagation:

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

		buttonsStyling: true,
		showCloseButton: true,
		closeButtonAriaLabel: 'cerrar alerta',


		// imageUrl:
		// imageWidth:
		// imageHeight:
		// imageAlt:

	}).then((result) => {
		if (result.value) {
			window.location.href = "{% url 'pages/inicio' %}"
		}
	});
});



// Add the following code if you want the name of the file appear on select
$(".custom-file-input").on("change", function () {
	var fileName = $(this).val().split("\\").pop();
	$(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});


$(document).ready(function () {
	$('[data-toggle="tooltip"]').tooltip();
});


$("#alertc1,#alertc2,#alertc3,#alertc4,#alertc5,#alertc6").click(function () {
	Swal.fire({
		title: '<span class="alerttit">Agregado</span>',
		text: 'La bicicleta ha sido añadida al carrito de alquiler correctamente',
		// html:
		icon: 'success',
		confirmButtonText: 'Ver tu carrito',
		// footer:
		// width:
		padding: '2rem',
		// background:
		// grow:
		//backdrop: false,
		// timer:
		// timerProgressBar:
		// toast:
		// position:
		// allowOutsideClick:
		// allowEscapeKey:
		// allowEnterKey:
		// stopKeydownPropagation:

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

		buttonsStyling: true,
		showCloseButton: true,
		closeButtonAriaLabel: 'cerrar alerta',


		// imageUrl:
		// imageWidth:
		// imageHeight:
		// imageAlt:

	}).then((result) => {
		if (result.value) {
			window.location.href = '#'
		}
	});
});



$(document).ready(function () {
	$("#myInput").on("keyup", function () {
		var value = $(this).val().toLowerCase();
		$("#myTable tr").filter(function () {
			$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
		});
	});
});



$(document).ready(function () {
	$('[data-toggle="tooltip"]').tooltip();
});






