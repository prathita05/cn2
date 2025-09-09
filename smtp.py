import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail account details
sender_email = "your_email@gmail.com"   ##replace
app_password = "your_16_char_app_password"   # not your normal Gmail password
receiver_email = "receiver_email@gmail.com"  ##replace (gmail to be sent to).

# Create email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email via Gmail SMTP"

# Add email body
body = "Hello! This is a test email sent from Python using Gmail SMTP."
msg.attach(MIMEText(body, "plain"))

# Connect to Gmail SMTP
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # upgrade to secure connection
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("✅ Email sent successfully!")
