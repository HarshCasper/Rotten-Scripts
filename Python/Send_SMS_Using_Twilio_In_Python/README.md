# Send SMS using Twilio in Python

A python script to send SMS using Twilio client.

## Setup

### 1. Create your Twilio account
![signup img](https://github.com/SANKET7738/test/blob/master/setup-imgs/signup.png)

### 2. code setup

1.This script requires **python3** or above. Check your python version by using command ```python --version```.  
2. Install the dependencies by ```pip install -r requirements.txt``` or just ```pip install twilio```.  
3. Now open the code in your code editor.  
4. Open your twilio account console.  

![console img](https://github.com/SANKET7738/test/blob/master/setup-imgs/console.png)

5. From here get your Twilio phone no, account sid and your auth token. Replace them at their respective places in the code.
6. In the message put the body as the what you want to send as the body of the SMS.
7. set value ```from_``` to your twilio phone number.
8. send ```to``` to the phone number of the receiver.
9. Now your done just use the command ```python script.py``` to run the script!

**Note-** The amount of SMS you can send, to whom you sent all depends on the type of your Twilio account. The trial account comes with a limited usage.
