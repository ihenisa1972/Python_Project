import smtplib, ssl
from email.mime.txt import MIMEText
from eail.mime.multipart import MIMEMultipart

# Setting up secured connection

sender_email = "ihenisa1972@gmail.com"
receiver_email = "ihenisapython@gmail.com"
password = input("Type your password and press enter: ")


message = """\
Subject: Hi there

This message is sent from Python."""

port = 465  # For SSL


# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("ihenisapython@gmail.com",password)
    server.sendmail(sender_email, receiver_email, message)