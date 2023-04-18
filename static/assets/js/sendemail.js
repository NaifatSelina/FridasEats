function sendEmail(contactForm) {
    event.preventDefault()
    console.log("Sending an email... ")
    emailjs.send("service_i73601k", "template_fgjkd8n", {
            "from_name": contactForm.first_name.value + " " + contactForm.last_name.value,
            "from_email": contactForm.emailaddress.value
        })
        .then(
            function (response) {
                console.log("SUCCESS", response);
                location.reload(); // Reload the current page after successful submission
                window.scrollTo(0, 0); // Scroll to the top of the page
            },
            function (error) {
                console.log("FAILED", error);
            }
        );
    return false; // To block from loading a new page
}