import sys
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
import mimetypes


class MailEngine:
    def __init__(self, host, port):
        """Initialize:
        Initializes Mass Mail Engine with given 2 arguments:
            1. HOST
            2. PORT
        """
        self.mail = SMTP(host=host, port=port)
        self.senderMail = ""
        self.mailSubject = ""
        self.mailFrom = ""
        self.mailTo = ""
        self.MimeText = ""
        self.mailPlainText = ""
        self.mailHTMLText = ""
        print(
            "\n-----+------+------+------+------+------+------+------+------+------+------"
        )
        print("                    MassMail Engine initialized")
        print(
            "-----+------+------+------+------+------+------+------+------+------+------\n"
        )

    def login(self, sender_mail, sender_password):
        """Login:
        Logs in into sender's mail account if given valid credentials
        """
        self.senderMail = sender_mail
        print("Logging in with registered email: {}".format(sender_mail))
        try:
            self.mail.ehlo()
            self.mail.starttls()
            self.mail.login(sender_mail, sender_password)
            print("Logged in successfully")
        except Exception as e:
            print("Error in login....")

    def addMessage(self, Text, MIMEType):
        """Add Message:
        Saves the MIMEType of the rendered template data as per the type of MIME:
            1. html
            2. plain
        """
        if MIMEType.lower() == "plain":
            self.mailPlainText = Text
        elif MIMEType.lower() == "html":
            self.mailHTMLText = Text
        else:
            print(
                "\n-----+------+------+------+------+------+------+------+------+------+------"
            )
            print("                         Error")
            print(
                "-----+------+------+------+------+------+------+------+------+------+------"
            )
            print("Error in MIME Type argument")
            print("Exiting program...")
            print(
                "-----+------+------+------+------+------+------+------+------+------+------\n"
            )
            sys.exit()

    def attachFile(self):
        """Attach file:
        Attaches additional files inside the MIMEMultipart script
        """
        pass

    def send(self, Subject, Sender, Reciever):
        """Send:
        Sends Email finally when templates are all passed and saved correctly to the corresponding variables
        """
        self.MIMEMultipartText = MIMEMultipart("alternative")
        self.MIMEMultipartText["Subject"] = Subject
        self.MIMEMultipartText["From"] = Sender
        self.MIMEMultipartText["To"] = Reciever

        if self.mailPlainText != "":
            self.MIMEMultipartText.attach(self.mailPlainText)
        elif self.mailHTMLText != "":
            self.MIMEMultipartText.attach(self.mailHTMLText)

        Message = self.MIMEMultipartText.as_string()
        self.mail.sendmail(Sender, Reciever, Message)

    def quitEngine(self):
        """Quit Engine:
        Clears memory of the instance of the class once all operations are complete
        """
        self.mail.quit()
