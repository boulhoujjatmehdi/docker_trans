
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	console.log("signup");
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});



	
document.getElementById('myForm').addEventListener('submit', function(event) {
	console.log("submit form checked in!");
	// Prevent the default form submission
	event.preventDefault();
	
	// Get the form data
	var formData = new FormData(event.target);

	const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
	// Send the form data using fetch
	fetch('http://localhost:8000/api/login/', {
		method: 'POST',
		body: formData,
		credentials: 'include',
		headers:{
		 'X-CSRFToken': csrfToken,			
		}
	})
	.then(response => response.json())  // Parse the JSON from the response
	.then(data => {
		// Handle the data from the response
		console.log(data);
	})
	.catch(error => console.error('Error:', error));
});



async function fetchCsrfToken() {
	const response = await fetch('http://localhost:8000/api/csrf-token/', {
		credentials: 'include'
	});
	const data = await response.json();
	return data.csrfToken;
}

fetchCsrfToken().then(csrfToken => {
	

	document.querySelector('meta[name="csrf-token"]').setAttribute('content', csrfToken);

	console.log(csrfToken);
});
	
