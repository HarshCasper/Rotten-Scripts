#!/usr/bin/python

import smtplib
import getpass

# The smtp module (Simple Mail Transfer Protocol) enables sending emails in python
# The sender's email must be configured to less secure apps.
# This configuration can be made on visiting account information.
# Under the category security, less secure apps must turned on

# "Sender's Email-ID"
sender_email = input("Enter the sender's Email-ID : ")

# "Receiver's Email-ID"
receiver = input("Enter the receiver's Email-ID : ")

# "Sender's password"
password = getpass.getpass(prompt='Enter the sender's password : ')
                           
# "Subject of the Email"
subject = input("Enter the subject of the email : ")

# "Content of the email"
body_of_the_email = input("Enter the content of the email : ")

content = "Subject: {}\n\n{}".format(subject, body_of_the_email)

# Specifications of the Email

server = smtplib.SMTP("smtp.gmail.com", 587)

# Here the Gmail service is used, a different Email service can also be used
# The port 587, across which the email is sent

server.starttls()
server.login(sender_email, password)

# Login is authorised

print("Login success")

server.sendmail(sender_email, receiver, content)
print("Email sent to the receiver")

# Email is sent, prints success on sending the email
