#!/usr/bin/python

import smtplib

#The smtp module (Simple Mail Transfer Protocol) enables sending emails in python
#The sender's email must be configured to less secure apps.
#This configuration can be made on visiting account information.
#Under the category security, less secure apps must turned on

def send_confirmation(sender_email, receiver_email, password, price_range):

    #Subject of the Email
    subject = "Amazon product price "

    if len(price_range) == 1: 
        cost = "The cost of the product is" + str(price_range[0])
    else:
        cost = "The cost of the product is within the range " + str(price_range[0]) + " and " + str(price_range[1])

    #Content of the email
    body_of_the_email = "Hello, This is to inform you that the price of the product you were looking for on Amazon is well-within your budget." + cost + " You can buy it right away."

    content = "Subject: {}\n\n{}".format(subject, body_of_the_email)

    #Specifications of the Email

    server = smtplib.SMTP("smtp.gmail.com" , 587)

    #Here the Gmail service is used, a different Email service can also be used
    #The port 587, across which the email is sent

    server.starttls()
    server.login(sender_email, password)

    #Login is authorised
    server.sendmail(sender_email, receiver_email, content)

    #Email is sent, prints success on sending the email

