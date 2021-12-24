import argparse
import sys
import time
from MassEmailSender.utils import register, sendMail

version = "1.0.0"


def intro():
    print("------+------+-------+-------+------+------+------+------+------+------")
    print("                        Mass-Email-Sender")
    print("------+------+-------+-------+------+------+------+------+------+------")
    time.sleep(1)


def main():
    intro()
    parser = argparse.ArgumentParser(
        description="Send Emails faster to masses in just one command"
    )
    subparser = parser.add_subparsers(title="commands", dest="command")

    # Version
    parser.add_argument("-v", action="version", version=version)

    # Commands
    """ Register:
        Register your email id and password with this command
    """
    parser_register = subparser.add_parser("register", help="Register your credentials")
    # Register Sender's Email id
    parser_register.add_argument("-id", type=str, help="Enter sender's email id")
    # Register Sender's Email password
    parser_register.add_argument("-pwd", type=str, help="Enter sender's email password")

    """ Send:
        Send Email by rendering templates- HTML/Text documents to a list of recievers from a CSV file
    """
    parser_send = subparser.add_parser(
        "send", help="Send emails to masses using this command"
    )

    # Add SUBJECT:
    parser_send.add_argument("-sub", type=str, help="Add Subject")
    # Render HTML
    parser_send.add_argument("-html", type=str, help="Render html templates")
    # Render Text Documents
    parser_send.add_argument("-text", type=str, help="Render text files as templates")
    # Path to Email reciever's list from CSV
    parser_send.add_argument(
        "-path",
        type=str,
        help="Path to CSV file containing list of reciever's email ids",
    )

    try:
        args = parser.parse_args()
        if args.command == "register":
            # Register mail id and password
            register(args.id, args.pwd)
            print(
                "------+------+-------+-------+------+------+------+------+------+------"
            )
        elif args.command == "send":
            # Send mail with rendered template
            if args.sub is not None and args.html is not None and args.path is not None:
                sendMail(args.sub, args.html, args.path)
            elif (
                args.sub is not None and args.text is not None and args.path is not None
            ):
                sendMail(args.sub, args.text, args.path)
            else:
                print(
                    "------+------+-------+-------+------+------+------+------+------+------"
                )
                print("                             Error Occured")
                print(
                    "------+------+-------+-------+------+------+------+------+------+------"
                )
                print("Add SUBJECT")
                print("Add the template file (.txt or .html)")
                print("Add the path to CSV")
                print(
                    "------+------+-------+-------+------+------+------+------+------+------"
                )
                sys.exit()
        else:
            print(
                "------+------+-------+-------+------+------+------+------+------+------"
            )
            print("                             Error Occured")
            print(
                "------+------+-------+-------+------+------+------+------+------+------"
            )
            print("No commands provided...")
            print("Type python mass_email_sender.py -h")
            print(
                "------+------+-------+-------+------+------+------+------+------+------"
            )
            sys.exit()

    except Exception as e:
        print("------+------+-------+-------+------+------+------+------+------+------")
        print("                             Error Occured")
        print("------+------+-------+-------+------+------+------+------+------+------")
        print("Command not found. Check the input commands again.\n")
        print("------+------+-------+-------+------+------+------+------+------+------")
        sys.exit()


if __name__ == "__main__":
    main()
