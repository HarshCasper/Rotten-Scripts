#! /usr/bin/env node

const inquirer = require('inquirer')
const auth = require('./auth')
let { authorization } = auth

//Package that enables sending of emails in Javascript
//npm install must be perfomed, in order to obtain all the modules
//In order to send the email successfully, the sender needs to enable "less secure apps" settings in the mail service used.

inquirer
.prompt([
        // Asks the user about their email
        {
                type: 'input',
                name: 'email',
                message: 'Enter your email:'
        },
])
.then(answers => {
        let email = answers.email
        // Asks the user the password of their email
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
                // Asks the user about the receiver's email
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
                        // Asks the user about the subject of the mail
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
                                // Asks the user to write the message that is needed to be sent to the receiver
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

                                        let mailDetails = { 
                                                from: email, 
                                                to: to, 
                                                subject: subject, 
                                                text: message
                                        };

                                        authorization(email, password, mailDetails)
                                });
                        });
                });
        }); 
});

