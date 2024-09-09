import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Define email sender and receiver
sender_email = "youremail@gmail.com"
receiver_email = "receiveremail@gmail.com"
password = "yourpassword"  # For Gmail, you might need an App Password

# Create the email subject and body
subject = f"Automated Email - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
body = "This is an automated email sent by the Python script."

# Create the email headers and message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the email body
message.attach(MIMEText(body, "plain"))

# Send the email using SMTP
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
