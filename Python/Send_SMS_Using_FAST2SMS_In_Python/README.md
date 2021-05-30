<h2>SMS-Sender</h2>

This is SMS sender project using Fast2SMS in Python. 
The main purpose of this project is to send sms efficiently using Python promptly to any number of your choice with the user specified text message

<h3>✔Instructions on how code is implemented:</h3>

1. Import the required libraries
2. To send sms we need an API. Here we use a Fast2SMS API as gateway for successful transmission of messages.
3. We provide the respective url of Fast2SMS and parameters like authorization, sender_id, route, language in the declaration. You can get all these details from Fast2SMS.
4. To acquire these details, you have to sign up in [FastSms](https://www.fast2sms.com/). Then go to Dev API and select the API key Tab and click generate. The API key is generated successfully
5. Now come to Dev API tab, you can see the syntax of how parameters can be declared. To know the declaration of parameters, you can refer to [Fast2SMS API Documentation](https://docs.fast2sms.com/). 
6. You can head to Quick SMS API. And further into POST method, as this method is secure for messages sending. 
7. Here the parameter details are given to ensure the flow of messages. It can be declared in a code. As you can see in a code, that I haven't mentioned number or message for flexibility.
8. Responses are directed to the JSON file.
9. Define a button to get a message to check if message is sent or not using btn_clk function
10. I have now created GUI interface with labels, extnumber and textmessages with the required specifications. I have also declared the send and quit button for operations and directed it to btn_clk. 
11. I have also placed a SMS logo to appear on GUI. Make sure the file is in this folder.

<h3>💡Demo of my Project:</h3>

![SMS_Sender](https://github.com/prathimacode-hub/Pythonista_ForAll/blob/main/SMS_Sender/SMS_Sender.png)
