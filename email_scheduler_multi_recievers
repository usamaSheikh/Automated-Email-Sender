import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Define email sender and list of receivers
sender_email = "youremail@gmail.com"
receiver_emails = ["receiver1@gmail.com", "receiver2@gmail.com", "receiver3@gmail.com"]  # List of recipient emails
password = "yourpassword"  # Gmail App Password if 2FA is enabled

# Create the email subject and body
subject = f"Automated Email - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
body = "This is an automated email sent by the Python script."

# Create the email headers and message
message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Convert the list of receiver emails to a comma-separated string
message["To"] = ", ".join(receiver_emails)

# Send the email using SMTP
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    
    # Loop through each receiver email and send the email
    for receiver in receiver_emails:
        server.sendmail(sender_email, receiver, text)
    
    server.quit()
    print("Emails sent successfully!")
except Exception as e:
    print(f"Failed to send emails: {e}")
