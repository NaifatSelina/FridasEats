// Initialize the review modal
var modal = document.querySelector('#id01');
var instance = new bootstrap.Modal(modal);

// Get the form element and add a submit event listener
var form = document.querySelector('#review-form');
form.addEventListener('submit', function (event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get the form data
    var formData = new FormData(form);

    // Send the form data to the server
    fetch('/submit-review', {
            method: 'POST',
            body: formData
        })
        .then(function (response) {
            // Display a success message
            var toast = new bootstrap.Toast(document.querySelector('.toast'));
            toast.show();

            // Reset the form
            form.reset();

            // Close the modal
            instance.hide();
        })
        .catch(function (error) {
            // Display an error message
            var toast = new bootstrap.Toast(document.querySelector('.toast'));
            toast.show();
        });
});