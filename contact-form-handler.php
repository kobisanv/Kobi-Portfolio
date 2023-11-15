<?php

// Include PHPMailer classes
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'Exception.php';
require 'PHPMailer.php';
require 'SMTP.php';

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Recipient email address
    $recipientEmail = "kobisan.vinotharupan@gmail.com";

    // Get sender's email, subject, and message from the POST data
    $senderEmail = $_POST["email"];
    $subject = $_POST["subject"];
    $message = $_POST["message"];

    try {
        // Create a new PHPMailer instance
        $mail = new PHPMailer();

        // Configure SMTP settings
        $mail->isSMTP();
        $mail->Host = 'smtp.gmail.com';
        $mail->Port = 587;
        $mail->SMTPSecure = 'tls'; // Enable TLS encryption
        $mail->SMTPAuth = true;
        $mail->Username = 'kobisan.vinotharupan@gmail.com'; // Your Gmail email address
        $mail->Password = 'svcx futa jbih lxxp'; // Your generated App Password

        // Set sender, recipient, subject, and email body
        $mail->setFrom($senderEmail);
        $mail->addAddress($recipientEmail);
        $mail->Subject = $subject;

        // Construct email body with sender's email and message
        $emailBody = "From: $senderEmail\n\n"; // Include sender's email in the body
        $emailBody .= $message;
        $mail->Body = $emailBody;

        // Send email and redirect to success page if successful
        if ($mail->send()) {
            header("Location: emailsuccess.html");
            exit;
        } else {
            // If sending fails, redirect to not-success page
            throw new Exception($mail->ErrorInfo);
        }
    } catch (Exception $e) {
        // If an exception occurs, redirect to not-success page with error message
        header("Location: emailnotsuccess.html");
    }
} else {
    // If it's not a POST request, display "Invalid request"
    echo "Invalid request";
}

