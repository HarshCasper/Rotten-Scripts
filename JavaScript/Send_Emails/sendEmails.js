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
                message: 'Enter your email:'
        },
])
.then(answers => {
        let email = answers.email
        // console.info('Answer:', answers.email);
        
        // This function gets the password of the mail from the user
        
        inquirer
        .prompt([
                {
                        type: 'input',
                        name: 'password',
                        message: 'Enter your password:'
                },
        ])
        .then(answers => {
                let password = answers.password
                // console.info('Answer:', answers.password);
                
                console.log(password + " " + email)
                
                // login(email, password)
                let login_and_auth = nodemailer.createTransport({ 
                        service: 'gmail',
                        //Any email service can be used here
                        auth: { 
                                user: email, 
                                pass: password
                        } 
                }); 
                
                inquirer
                .prompt([
                        {
                                type: 'input',
                                name: 'to',
                                message: "Enter the receiver's email:"
                        },
                ])
                .then(answers => {
                        let to = answers.to
                        // console.info('Answer:', answers.to);

                        inquirer
                        .prompt([
                                {
                                        type: 'input',
                                        name: 'subject',
                                        message: "Enter the subject:"
                                },
                        ])
                        .then(answers => {
                                let subject = answers.subject
                                // console.info('Answer:', answers.subject);

                                inquirer
                                .prompt([
                                        {
                                                type: 'input',
                                                name: 'body',
                                                message: "Enter the message:"
                                        },
                                ])
                                .then(answers => {
                                        let message = answers.message
                                        // console.info('Answer:', answers.message);

                                        let mailDetails = { 
                                                from: 'every1isnotrupangkan@gmail.com', 
                                                to: to, 
                                                subject: subject, 
                                                text: message
                                        };

                                        //This function consists of the details of the email

                                        login_and_auth.sendMail(mailDetails, function(err, data) { 
                                                if(err) { 
                                                        console.log(err.message)
                                                        console.log('Unable to send the email'); 
                                                } 
                                                else    { 
                                                        console.log('Email sent'); 
                                                } 
                                        }); 
                                        
                                        //This function makes a connection with the server and sends the email.

                                });
                        });
                });

              
                        
                
        }); 
        
});

//In order to send the email successfully, the sender needs to enable "less secure apps" settings in the mail service used.
