# Email_Spammer
Undetected Email Spammer Program


Email Sending Process

The sendEmail(message) function handles the process of sending an email:

    It establishes a connection to the Gmail SMTP server.
    It starts a TLS (Transport Layer Security) connection to ensure that the email content is encrypted.
    It logs into the sender's email account using the provided credentials.
    It sends the email to the specified receiver.
    It handles any exceptions that may occur during the process and ensures the connection to the SMTP server is closed in the finally block.

Message Sending

The message to be sent is fetched from the spammer file that contains the desired text.

How to Use

    Ensure you have the required Python libraries: The script relies on built-in Python libraries, so no external dependencies are needed beyond your spammer module.
    Update the email addresses and password: Before running the script, make sure to replace the sender_email, receiver_email, and password with your actual details.
    Run the script: Execute the script to send the email and measure the time taken.

Note: Make sure you have enabled "Less secure app access" in your Gmail account or set up an App Password if you have 2-Step Verification enabled.
Security Warning

Hardcoding email credentials directly in the script is not recommended for production use as it poses a security risk. Consider using environment variables or a secure vault service to manage sensitive information.
