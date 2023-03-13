
function clear(){
    tittle.value = "";
    genres.value = "";
    authors.value = "";
}

function hide() {
    form.style.display = "none";
}

function show(){
    form.style.display = "";
}

// form.onsubmit = onSubmitClicked;

 clearButton.onclick = clear;
 hideButton.onclick = hide;
 showButton.onclick = show;

 //--------------------------------


const form = document.querySelector('#createForm');
		form.addEventListener('submit', (event) => {
			// Detiene el envío del formulario
			event.preventDefault();
			// Verifica que todos los campos requeridos estén completos
			if (form.checkValidity() === false) {
				event.stopPropagation();
			} else {
				// Enviar formulario
				form.submit();
			}
			form.classList.add('was-validated');
		})

		// funcion asincrona para ver una web
		async function redirect() {
			await fetch('https://www.casadellibro.com/');
			window.location.href = 'https://www.casadellibro.com/';
			
		  }

		// funcion flecha 
		const createBtn = document.getElementById('create-btn');

		createBtn.addEventListener('click', () => {
  		window.location.href = '/';
		});
		  
		  
		  
		  
		  
		
		
		  




		// Agrega la validación de género
		// const genreInput = document.querySelector('#genre');
		// genreInput.addEventListener('change', (event) => {
		// 	const selectedGenre = event.target.value;
		// 	if (selectedGenre === '') {
		// 		genreInput.setCustomValidity('Por favor, selecciona un género');
		// 	} else {
		// 		genreInput.setCustomValidity('');
		// 	}
		// })

		