const nodemailer = require('nodemailer'); 
//Package that enables sending of emails in Javascript
//After performing npm init, npm install nodemailer must be perfomed, in order to obtain all the modules

let login_and_auth = nodemailer.createTransport({ 
        service: 'gmail',
        //Any email service can be used here
        auth: { 
                    user: 'sender', 
                    pass: '******'
                } 
}); 
//This function authorises login 

let mailDetails = { 
        from: 'sender', 
        to: 'receiver', 
        subject: 'subject', 
        text: 'body of email'
}; 

//This function consists of the details of the email

login_and_auth.sendMail(mailDetails, function(err, data) { 
        if(err) { 
                    console.log('Enable to send the email'); 
                } 
        else    { 
                    console.log('Email sent'); 
                } 
}); 

//This function makes a connection with the server and sends the email.


//In order to send the email successfully, the sender needs to enable "less secure apps" settings in the mail service used.
