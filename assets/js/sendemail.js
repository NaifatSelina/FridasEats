function sendEmail(contactForm) {
    email.js.send("service_i73601k", "template_fgjkd8n", {
        "from_name": contactForm.first_name.value,
        "from_email": contactForm.emailaddress.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false; 
}