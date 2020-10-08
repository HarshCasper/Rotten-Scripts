# MassEmailSender

Send mails to masses by rendering Text files and HTML templates.

# Prerequisites:

- Create a CSV file, say `mails.csv` consisting a column, `Email`, spelled as it is, and add the list of all the receiver's email to be sent in
  that column.

          Email
          abc@gmail.com
          pqr.we@outlook.com
          xyz@yahoo.com

- Create a Template that you want to send to the receivers.
  This can be:

  - A TEXT file &emsp;(sample shown [here](templates/sample.txt))
  - Or a HTML file &emsp;(sample shown [here](templates/sample.html))

- Enable Less Secured Apps from your google account, [click here](https://myaccount.google.com/lesssecureapps)
  - This needs to be enabled as Python needs to login to your email account which requires permissions from your google account.
- Disable it once your mails are sent.

# Usage:

### Install Requirements:

- Install all the requirements in the requirements.txt file

        pip install -r requirements.txt

### Register Sender's Email:

- Provide valid credentials using a simple command

        python mass_email_sender.py register -id "Your-Email-Id" -pwd "Corresponding-Mail-Password"

such as:

        python mass_email_sender.py register -id abc@gmail.com -pwd abc1234

### Send Mail By Rendering Templates from TEXT files `(.txt)`:

        python mass_email_sender.py send -sub "Type the subject here" -text "Path-to-Text-File" -path "Path-to-CSV-File"

such as:

        python mass_email_sender.py send -sub "Letter of Recommendation" -text templates/sample.txt -path mails.csv

### Send Mail By Rendering Templates from HTML files `(.html)`:

        python mass_email_sender.py send -sub "Type the subject here" -text "Path-to-HTML-File" -path "Path-to-CSV-File"

such as:

        python mass_email_sender.py send -sub "Letter of Recommendation" -text templates/sample.html -path mails.csv
