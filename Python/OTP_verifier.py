import random
from twilio.rest import Client

otp=random.randint(1000,9999)
print(otp)
account_sid='Find from your twilio account'
auth_token='Finfd from your twilio account'
client=Client(account_sid,auth_token)

message=client.message.create(
body='Your OTP is-'+str(otp),
from_='Your trial number',
to='your phone number'
)
print(message.sid)
