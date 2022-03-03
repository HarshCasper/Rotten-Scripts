const nodemailer = require('nodemailer'); 


function authorization(email, password, mailDetails){

    // This part verifies the password of the mail from the user

    let login_and_auth = nodemailer.createTransport({ 
        service: 'gmail',
        //Any email service can be used here
        auth: { 
                user: email, 
                pass: password
        } 
    }); 

    //This part consists of the details of the to send to the receiver's mail
    //Also makes a connection with the server and sends the email.

    login_and_auth.sendMail(mailDetails, function(err, data) { 
        if(err) { 
                console.log(err.message)
                console.log('Unable to send the email'); 
        } 
        else    { 
                console.log('Email sent'); 
        } 
}); 
}

module.exports = {authorization: authorization}

