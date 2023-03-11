// Get the "Write a Review" button element from the DOM
const reviewBtn = document.getElementById("review-btn");

// Add an event listener to the button
reviewBtn.addEventListener("click", function(event) {
  // Prevent the default button click behavior
  event.preventDefault();

  // Show the modal
  const reviewModal = new bootstrap.Modal(document.getElementById("review-modal"));
  reviewModal.show();
});

// Initialize the modal
var modal = document.querySelector('#review-modal');
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
