import smtplib
import ssl
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.message import EmailMessage

load_dotenv()


def send_email(message, subject="A new email!"):
    host = os.getenv("HOST")
    port = 465

    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("EMAIL_RECEIVER")
    context = ssl.create_default_context()

    msg = EmailMessage()
    msg["Subject"] = subject
    msg.set_content(message)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())
