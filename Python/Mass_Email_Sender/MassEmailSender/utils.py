import sys

import pandas as pd
import os
from pathlib import Path
from MassEmailSender.engine import MailEngine
import time
import mimetypes
from email.mime.text import MIMEText

"""PATH"""
dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)
path_to_credentials = root / "credentials.txt"

"""CONFIGURATION"""
host = "smtp.gmail.com"
port = 587


"""Register:
    Registers Email-Id and Password and saves in 'credentials.txt' file
    *** Caution: This file contains your credentials, don't make it public ***
"""


def register(mail_id, password):
    if mail_id is None or password is None:
        print("Improper credentials given...")
    else:
        with open(path_to_credentials, "w") as f:
            f.write("{} {}".format(mail_id, password))
        print("Mail id registered successfully for '{}'".format(mail_id))


"""Load Credentials:
    Loads Credentials if registered (if credentials.txt file exists)
"""


def load_credentials():
    with open(path_to_credentials, "r") as f:
        data = f.read()

    mail_id = data.split(" ")[0]
    mail_pwd = data.split(" ")[1]
    print("Loaded registered credentials correctly.....")
    print("Registered email: {}".format(mail_id))
    return mail_id, mail_pwd


"""Load CSV:
    Loads CSV file consisting the list of emails in columns
    N.B.: The file must contain a column 'Email' under which all the mails must be listed
"""


def loadCSV(path):
    data = pd.read_csv(path)
    emails = []

    for email in data["Email"]:
        emails.append(email)
    return emails


"""Send Mail:
    Sends mails by loading all the files as input and renders the templates
"""


def sendMail(SUBJECT, template, data_path):
    try:
        reciever_email_list = loadCSV(data_path)
        senderMail, senderPassword = load_credentials()

        # render template
        render(SUBJECT, senderMail, senderPassword, reciever_email_list, template)
    except Exception as e:
        print(
            "\n------+------+-------+-------+------+------+------+------+------+------"
        )
        print("                           Error Occured")
        print("------+------+-------+-------+------+------+------+------+------+------")
        print("Oops an unknown error occured")
        print("Error reading in file")
        print("Check if you registered your credentials....")
        print("Check your input paths....")
        print("------+------+-------+-------+------+------+------+------+------+------")
        sys.exit()


"""Render:
    Render templates given as input in command-line
    Templates include:
        1. HTML
        2. Plain Text
"""


def render(SUBJECT, senderMail, senderPassword, reciever_email_list, template):
    temp_type = template.split(".")[-1]
    ctype, encoding = mimetypes.guess_type(template)
    maintype, subtype = ctype.split("/", 1)

    try:
        temp_data = open(template, "r", encoding="utf-8")
        body_msg = MIMEText(temp_data.read(), _subtype=subtype)

        if temp_type == "txt":
            print("Rendering Text Template")
            print(body_msg)
            renderTXT(
                SUBJECT, senderMail, senderPassword, reciever_email_list, body_msg
            )
            temp_data.close()

        elif temp_type == "html":
            print("Rendering HTML Template")
            print(body_msg)
            renderHTML(
                SUBJECT, senderMail, senderPassword, reciever_email_list, body_msg
            )
            temp_data.close()

        else:
            temp_data.close()
            print(
                "------+------+-------+-------+------+------+------+------+------+------"
            )
            print("                             Error Occured")
            print(
                "------+------+-------+-------+------+------+------+------+------+------"
            )
            print("Given file extension is neither of type '.html' or '.txt'")
            print("Check input file extension again...")
            print(
                "------+------+-------+-------+------+------+------+------+------+------"
            )
            sys.exit()

    except Exception as e:
        print("------+------+-------+-------+------+------+------+------+------+------")
        print("                             Error Occured")
        print("------+------+-------+-------+------+------+------+------+------+------")
        print("File not found Error")
        print("Improper file path given....Check input again")
        print("------+------+-------+-------+------+------+------+------+------+------")
        sys.exit()


"""Render HTML:
    Renders HTML Templates given as argument through command-line
"""


def renderHTML(Subject, senderMail, senderPassword, reciever_email_list, body_msg):
    try:
        # Initialize MassMailSender with host and Port
        mail = MailEngine(host=host, port=port)
        count = len(reciever_email_list)

        # Login to your email Account with given credentials
        mail.login(senderMail, senderPassword)

        print("------+------+-------+-------+------+------+------+------+------+------")
        print("                       Mails To be sent ({})".format(count))
        print("------+------+-------+-------+------+------+------+------+------+------")

        # Loop to Send Emails One-By-One
        for i in range(count):
            print("\n[Mail]({}) Sending to : {}".format(i + 1, reciever_email_list[i]))

            # Initialize
            SUBJECT = Subject
            SENDER = senderMail
            RECIEVER = reciever_email_list[i]

            # Mail Body
            HTMLText = body_msg

            # ## Insert Message either in the form of 'PlainText' or in the form of 'HTMLtext'
            mail.addMessage(Text=HTMLText, MIMEType="html")

            # ## Send Mail
            mail.send(Subject=SUBJECT, Sender=SENDER, Reciever=RECIEVER)

        # Exit MassMail Engine
        mail.quitEngine()

        time.sleep(1)
        print(
            "\n\n-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("                     All Mails sent successfully")
        print(
            "-----+------+------+------+------+------+------+------+------+------+------"
        )
        sys.exit()

    except Exception as e:
        print(
            "\n-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("                               Error")
        print(
            "-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("Oops!!! An error ocurred....Couldn't send mails")
        print("Error: {}".format(e))
        time.sleep(1)

        print(
            "\n---------------------Trouble Shooter---------------------------------------"
        )
        print("1. Check if Less Secured App is enabled")
        print("2. Check for a relatively strong internet connection.")
        print("3. Check validity for given sender credentials")

        time.sleep(1)
        print(
            "\n\n-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("                           Exiting Program")
        print(
            "-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("Exiting program...\n")
        print("------+------+-------+-------+------+------+------+------+------+------")
        sys.exit()


"""Render TEXT:
    Renders TEXT file Templates given as argument through command-line
"""


def renderTXT(Subject, senderMail, senderPassword, reciever_email_list, body_msg):
    try:
        # Initialize MassMailSender with host and Port
        mail = MailEngine(host=host, port=port)
        count = len(reciever_email_list)

        # Login to your email Account with given credentials
        mail.login(senderMail, senderPassword)

        print("------+------+-------+-------+------+------+------+------+------+------")
        print("                       Mails To be sent ({})".format(count))
        print("------+------+-------+-------+------+------+------+------+------+------")

        # Loop to Send Emails One-By-One
        for i in range(count):
            print("\n[Mail]({}) Sending to : {}".format(i + 1, reciever_email_list[i]))

            # Initialize
            SUBJECT = Subject
            SENDER = senderMail
            RECIEVER = reciever_email_list[i]

            # Mail Body
            PlainText = body_msg

            # ## Insert Message either in the form of 'PlainText' or in the form of 'HTMLtext'
            mail.addMessage(Text=PlainText, MIMEType="plain")

            # ## Send Mail
            mail.send(Subject=SUBJECT, Sender=SENDER, Reciever=RECIEVER)

        # Exit MassMail Engine
        mail.quitEngine()

        time.sleep(1)
        print(
            "\n\n-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("                     All Mails sent successfully")
        print(
            "-----+------+------+------+------+------+------+------+------+------+------"
        )
        sys.exit()

    except Exception as e:
        print(
            "\n-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("                               Error")
        print(
            "-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("Oops!!! An error ocurred....Couldn't send mails")
        print("Error: {}".format(e))
        time.sleep(1)

        print(
            "\n---------------------Trouble Shooter---------------------------------------"
        )
        print("1. Check if Less Secured App is enabled")
        print("2. Check for a relatively strong internet connection.")
        print("3. Check validity for given sender credentials")

        time.sleep(1)
        print(
            "\n\n-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("                           Exiting Program")
        print(
            "-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("Exiting program...\n")
        print("------+------+-------+-------+------+------+------+------+------+------")
        sys.exit()
