#import necessary files

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import smtplib

MY_ADDRESS = ""   #Your Email ID
PASSWORD = ""      #Password to your email id {Do not share}

#function to read contacts from a given contact 
# file and return list of names and email adress

def get_contacts(filename):  
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

#funtion to read template files

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

#to check if smptp mail box is outlook or gmail
#and configure accordingly

if 'outlook' in MY_ADDRESS:
    host_string = "smtp-mail.outlook.com"
    port_num = 587
elif 'gmail' in MY_ADDRESS:
    host_string = "imap.gmail.com"
    port_num = 993

#setup smptp server

s = smtplib.SMTP(host=host_string, port=port_num)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
message_template = read_template('message.txt')
names, emails = get_contacts('mycontacts.txt')

#parsing each contact in mycontacts.txt and sending them email

for name, email in zip(names, emails):
    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name.title())
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="This is a test program"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg