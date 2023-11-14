import emailjs from "https://cdn.emailjs.com/dist/email.min.js"
emailjs.init('yZVvJf75mMKn1rwV0');
const form = document.querySelector("#contact-form");

function sendEmail() {
    console.log('Form element:', form);
    if (form) {
        emailjs.sendForm("service_jj1bdmt", "template_uls72su", form, 'yZVvJf75mMKn1rwV0')
            .then (
                function(response) {
                    console.log('Email sent successfully: ', response);
                    window.location.href = "emailsuccess.html";
                },
                function(error) {
                    console.error('Email not sent. Error: ', error);
                    window.location.href = "emailnotsuccess.html";
                }
            );
    } else {
        console.error('Form element not found');
    }
}

// Attach sendEmail function to the button click event
const submitBtn = document.getElementById("submitBtn");
if (submitBtn) {
    submitBtn.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent default form submission
        console.log("Button was clicked");
        sendEmail(); // Call sendEmail function
    });
}