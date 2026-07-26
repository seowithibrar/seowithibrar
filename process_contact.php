<?php
header('Content-Type: application/json');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate inputs
    $fullname = htmlspecialchars(trim($_POST['fullname'] ?? ''));
    $email = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
    $website = htmlspecialchars(trim($_POST['website'] ?? ''));
    $location = htmlspecialchars(trim($_POST['location'] ?? ''));
    $goals = htmlspecialchars(trim($_POST['goals'] ?? ''));

    if (empty($fullname) || empty($email)) {
        echo json_encode(["success" => false, "message" => "Name and Email are required."]);
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo json_encode(["success" => false, "message" => "Invalid email format."]);
        exit;
    }

    // Email configuration
    $to = "ibrarahmad0304@gmail.com";
    $subject = "New SEO Consultation Request from $fullname";
    
    // Email body
    $body = "You have received a new consultation request from your website.\n\n";
    $body .= "Full Name: $fullname\n";
    $body .= "Email: $email\n";
    $body .= "Website: $website\n";
    $body .= "Target Location: $location\n";
    $body .= "Business Goals / Message:\n$goals\n";

    // Headers
    $headers = "From: noreply@seowithibrar.com\r\n"; // Using a noreply or the domain's email prevents spam issues often caused by spoofing the user's email
    $headers .= "Reply-To: $email\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();

    // Send email
    if (mail($to, $subject, $body, $headers)) {
        echo json_encode(["success" => true, "message" => "Email sent successfully."]);
    } else {
        echo json_encode(["success" => false, "message" => "Failed to send email. Please try again later."]);
    }
} else {
    echo json_encode(["success" => false, "message" => "Invalid request method."]);
}
?>
