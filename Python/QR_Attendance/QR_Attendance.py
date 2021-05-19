import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import base64
import sys
import time
import datetime
import xlwt
from xlwt import Workbook
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from decouple import config


capture_qr = cv2.VideoCapture(0)  # Opening camera
font = cv2.FONT_HERSHEY_PLAIN

attendace_file = open('attendence_log.txt', 'w+')

names = []
scan_time = []

Class_name= str(input("Which class is this? : "))
Teacher = str(input("Please enter Teacher's name : "))
Class_start = str(input("Thanks! {0}, At what time would you like to begin your class? : ".format(Teacher)))
Class_end = str(input("Noted!! At what time would you like to conclude your class? : "))
Class_time = Class_start +' - '+Class_end
receiver_address=str(input("We would like to mail you the attendance sheet. \n please Enter you email address : "))
print("Thanks! This attendance system is set for {0} class for {1} and attendance sheet will be mailed at {2}".format(
    Class_name, Class_time, receiver_address))


log_date = datetime.datetime.now()
date_format = log_date.strftime("%d-%m-%Y")
#Current_time = log_date.strftime("%I:%M:%S %p")
#date_format=date_format.replace(':',' ')
file_name = Class_name+' '+date_format+'.xls'

def Data_entry(student, log_date):
    if student in names:
        pass
    else:
        names.append(student)
        log_date = datetime.datetime.now()
        scan_time.append(log_date.strftime("%I:%M:%S %p"))
        student = ''.join(str(student))
        attendace_file.write(student+'\n')
    return names


def data_validation(data):
    try:
        data = str(base64.b64decode(data).decode())
    except(TypeError):
        print('Invalid ID ! \n please scan a valid QR')
        return
    if data in names:
        print("{0}'s attendance has been already marked".format(data))
    else:
        print('\n'+str(len(names)+1)+'\n'+data)
        Data_entry(data, log_date)
    cv2.putText(QR, str(base64.b64decode(qr_data.data)), (50, 50), font, 2,
                (255, 0, 0), 3)


def writeExcel(names, date_format, Class_name, scan_time, Class_time, file_name):

    wb = Workbook()

    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, Class_name+' class '+' by '+Teacher)
    sheet1.write(2, 0, 'Date:'+date_format)
    sheet1.write(2, 2, 'Class Time:'+Class_time)
    sheet1.write(4, 0, 'Sr.No')
    sheet1.write(4, 1, 'Names')
    sheet1.write(4, 2, 'ID')
    sheet1.write(4, 3, 'Time')
    for i in range(0, len(names)):
        sheet1.write(i+5, 0, i+1)
        name = names[i].split(' - ')
        sheet1.write(i+5, 1, name[0])
        sheet1.write(i+5, 2, name[1])
        sheet1.write(i+5, 3, scan_time[i])

    wb.save(file_name)


def send_mail(receiver_address, file_name):
    mail_content = '''Hello {0},E
    This is an auto-generated email.
    Attendance sheet is attached in this mail.
    Thank You'''.format(Teacher)
    # The mail addresses and password
    sender_address = config('Email')
    sender_pass = config('password')
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Attendance Sheet : {0}'.format(file_name)
    # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = file_name
    attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)  # encode the attachment
    # add payload header with filename
    payload.add_header('Content-Decomposition',
                       'attachment', filename=attach_file_name)
    message.attach(payload)
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


print('Ready to SCAN for attendace \n please scan your QR code')


while True:
    _, QR = capture_qr.read()

    decodedObjects = pyzbar.decode(QR)
    for qr_data in decodedObjects:
        data_validation(qr_data.data)

        time.sleep(1)

    cv2.imshow("QR_Attendance", QR)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

attendace_file.close()

writeExcel(names, date_format, Class_name,
           scan_time, Class_time, file_name)

time.sleep(3)

send_mail(receiver_address, file_name)
