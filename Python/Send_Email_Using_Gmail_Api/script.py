import os.path
import pickle
import base64
import argparse
import sys

from email.mime.text import MIMEText
from googleapiclient.discovery import build
from googleapiclient import errors


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    return {
        "raw": base64.urlsafe_b64encode(message.as_string().encode("utf-8")).decode(
            "utf-8"
        )
    }


def send_message(service, user_id, message):
    """Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    """
    try:
        message = (
            service.users().messages().send(userId=user_id, body=message).execute()
        )
        print("Message Id: %s" % message["id"])
        print(message)
    except errors.HttpError as error:
        print("An error occurred: %s" % error)


def main():
    """Shows basic usage of the Gmail API."""
    parser = argparse.ArgumentParser()
    parser.add_argument("to", help="Email address of the receiver")
    parser.add_argument("subject", help="The subject of the email message.")
    parser.add_argument("message_text", help="The text of the email message")
    args = parser.parse_args()
    reciver = args.to
    email_subject = args.subject
    email_content = args.message_text

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        print("Please run auth.py first to authorizer")
        sys.exit(1)

    service = build("gmail", "v1", credentials=creds)

    # Call the Gmail API
    sender = service.users().getProfile(userId="me").execute()["emailAddress"]
    message = create_message(sender, reciver, email_subject, email_content)
    send = send_message(service, "me", message)


if __name__ == "__main__":
    main()
