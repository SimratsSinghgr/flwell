#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import cgi
import cgitb

# Enable detailed error messages in the browser (for development)
cgitb.enable()
print("working")
# Get the user's email from the form
form = cgi.FieldStorage()
user_email = form.getvalue('email')

# Email server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Use the appropriate port for your server
smtp_username = 'simratbackupacc@gmail.com'
smtp_password = 'sycc rwzl rzas yhql'

# Sender and recipient emails
sender_email = 'simratbackupacc@gmail.com'
recipient_email = user_email

# Email content
subject = 'Email Confirmation'
message = 'Thank you for using our service!'

# Set up the MIME
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server and send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    #print('Content-type: text/html\n')
    print('Email sent successfully!')
except Exception as e:
    #print('Content-type: text/html\n')
    print(f'Error: {e}')
