import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Use SMTP over TLS
server = smtplib.SMTP('smtp.gmail.com', 587)  # Use port 587 for TLS
server.ehlo()
server.starttls()  # Start TLS encryption

# Read the password from a file
with open('password.txt', 'r') as f:
    password = f.read().strip()

# Log in to the server using your Gmail credentials
server.login('username1@gmail.com', password)

# Create the email
msg = MIMEMultipart()
msg['From'] = 'Name'
msg['To'] = 'username2@gmail.com'
msg['Subject'] = 'Just A Test'

# Read the message body from a file
with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

# Attach a file (e.g., a photo)
filename = 'photo.jpg'
with open(filename, 'rb') as attachment:
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

# Convert the message to a string and send it
text = msg.as_string()
server.sendmail('username1@gmail.com', 'username2@gmail.com', text)

# Quit the server
server.quit()
