# import the Twilio Client
from twilio.rest import Client

# your account sid
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# your auth id
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# to authenticate your account
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello! from Python", # the msg you want to send
                     from_='+126xxxxxxxx',      # your Twilio phone number
                     to='+91xxxxxxxx'         # the phone no you want send the SMS to
                 )

print(message.sid)
