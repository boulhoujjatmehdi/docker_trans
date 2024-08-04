
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



function getCsrfTokenFromCookie() {
	let cookieValue = null;
	let name = 'csrfToken';  // Replace this with the name of your CSRF token cookie
	if (document.cookie && document.cookie !== '') {
		let cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			let cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}



document.getElementById('signInForm').addEventListener('submit', function(event) {
	console.log("submit form checked in!");
	// Prevent the default form submission
	event.preventDefault();
	
	// Get the form data
	var formData = new FormData(event.target);
	
	// Send the form data using fetch
	fetch('http://localhost:8000/api/login/', {
		method: 'POST',
		body: formData,
		credentials: 'include'
	})
	.then(response => response.json())  // Parse the JSON from the response
	.then(data => {
		// Handle the data from the response
		showMessage(data.message, "signInMessage");

		console.log(data);
	})
	.catch(error => console.error('Error:', error));
});

function check_password(){
	pass1 = document.getElementById("register_pass_1");
	pass2 = document.getElementById("register_pass_2");
	if(pass1 == pass2)
		return true;
	else
		return false;

}

function showMessage(message, id)
{
	var elem = document.getElementById(id);
	elem.innerHTML = message;

	setTimeout(() => {
		elem.innerHTML = '';
	}, 3000);
}


document.getElementById('signUpForm').addEventListener('submit', function(event) {
	console.log("submit form checked in!");
	// Prevent the default form submission
	event.preventDefault();
	
	// Get the form data
	var formData = new FormData(event.target);

	if(check_password())
	{
		// Send the form data using fetch
		fetch('http://localhost:8000/api/register/', {
			method: 'POST',
			body: formData,
			credentials: 'include'
		})
		.then(response => response.json())  // Parse the JSON from the response
		.then(data => {
			// Handle the data from the response
			console.log(data);
		})
		.catch(error => console.error('Error:', error));
	}
	else
	{
		console.log("passwords not matched");
	}

});



