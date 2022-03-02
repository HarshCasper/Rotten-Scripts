const nodemailer = require('nodemailer'); 
const inquirer = require('inquirer')
//Package that enables sending of emails in Javascript
//npm install must be perfomed, in order to obtain all the modules

// This function gets the email of sender from the user

inquirer
.prompt([
        {
                type: 'input',
                name: 'email',
                message: 'Type your email:'
        },
])
.then(answers => {
        let email = answers.email
        console.info('Answer:', answers.email);
        
        // This function gets the password of the mail from the user

        inquirer
        .prompt([
                {
                        type: 'input',
                        name: 'password',
                        message: 'Type your password:'
                },
        ])
        .then(answers => {
                let password = answers.password
                console.info('Answer:', answers.password);

                console.log(password + " " + email)


                let login_and_auth = nodemailer.createTransport({ 
                        service: 'gmail',
                        //Any email service can be used here
                        auth: { 
                                user: email, 
                                pass: password
                        } 
                }); 

                //This function authorises login 


                let mailDetails = { 
                        from: 'Rupangkan', 
                        to: 'reposekalita@gmail.com', 
                        subject: 'subject', 
                        text: 'body of email'
                };
                
                //This function consists of the details of the email
                
                login_and_auth.sendMail(mailDetails, function(err, data) { 
                        if(err) { 
                                console.log(err)
                                console.log('Unable to send the email'); 
                        } 
                        else    { 
                                console.log('Email sent'); 
                        } 
                }); 
                
                //This function makes a connection with the server and sends the email.
                
        }); 
        
});



// console.log(password + " " + email)



//In order to send the email successfully, the sender needs to enable "less secure apps" settings in the mail service used.
