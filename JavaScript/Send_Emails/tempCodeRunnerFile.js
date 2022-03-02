let login_and_auth = nodemailer.createTransport({ 
//         service: 'gmail',
//         //Any email service can be used here
//         auth: { 
//                 user: email.toString, 
//                 pass: password.toString
//         } 
// }); 
// //This function authorises login 

// let mailDetails = { 
//         from: 'every1isnotrupangkan@gmail.com', 
//         to: 'reposekalita@gmail.com', 
//         subject: 'subject', 
//         text: 'body of email'
// }; 

// //This function consists of the details of the email

// login_and_auth.sendMail(mailDetails, function(err, data) { 
//         if(err) { 
//                 console.log('Unable to send the email'); 
//         } 
//         else    { 
//                 console.log('Email sent'); 
//         } 
// }); 