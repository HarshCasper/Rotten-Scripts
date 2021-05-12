const prompt = require("prompt-sync")()
const scrapper = require("./scrapper")
const chalk = require("chalk")

const displayEndorsements = (data) => {
    for (let i = 0; i < data.length; i++) {

        console.log(`${i + 1}. ${chalk.yellow(data[i]["skill"])}`);
        console.log(`Endorsements: ${chalk.yellow(data[i]["number"])}`);
        console.log(`People:`);
        for (let j = 0; j < data[i]["people"].length; j++) {
            console.log(`\t${chalk.green(data[i]["people"][j])}`);
        }
        console.log("\n");

    }
}

const init = async () => {
    /**
     * 1. get LinkedIn profile link
     * 2. scrape endorsements
     * 3. display them
     */
    console.log("\n===================================");
    console.log("---LinkedIn Endorsement scrapper---");
    console.log("===================================\n");

    let profileLink = "https://www.linkedin.com/in/kunal-kushwaha/"//prompt("Enter LinkedIn profile link : ")

    // let endorsements = await scrapper.getEndorsements(profileLink)
    endorsements = [
        {
            skill: 'DevOps',
            people: [
                'Ankush Singh Gandhi',
                'Akash Rao Mallareddy',
                'Preksha Shetti',
                'Prathamesh Sankpal',
                'Vaibhavi Thirukovela',
                'Ramswaroop Padhy',
                'Rutuja Konde',
                'Surinder Choudhary',
                'Ashish kashyap',
                'Devesh Anand Srivastava',
                'Rajit Paul',
                'Harsh Koli',
                'Akash Chetia',
                'Prudhvi Naidu',
                'Rishabh Sachdeva',
                'Abhinav Mishra',
                'Yashas K S',
                'Manbir Singh Marwah',
                'Ramdev C M',
                'Himanshu Malik',
                'Atharva Bet',
                'Manav Chaudhary',
                'Ankit Aggarwal',
                'Priyansh Neema',
                'Ritvik Shukla',
                'Fuzail Kazi',
                'ARYAN GULATI',
                'Vishal Rajput',
                'Divija Babhravi Singh',
                'Raj Aryan Singh',
                'Akash Jyoti Sahoo',
                'Srinjoy Ganguly',
                'Shikhar Srivastava',
                'Kriti Bhaskar ( Elima Sharma )',
                'Rahul Bera',
                'Aishwarya N.',
                'Abhishek Bansal',
                'Sai Sonali',
                'Kajal Jha'
            ],
            number: 39
        },
        {
            skill: 'Web Development',
            people: [
                'Ankush Singh Gandhi', 'Preksha Shetti',
                'Abdul Qadir', 'Prathamesh Sankpal',
                'Abhishek Bharti', 'Rishabh Shrivastava',
                'Prankur Gupta', 'Divyansh Sharma',
                'Akash Chetia', 'Himanshu Malik',
                'Manbir Singh Marwah', 'ADITYA AGRAWAL',
                'Ankit Aggarwal', 'Raj Karan Singh',
                'ARYAN GULATI', 'Vishal Rajput',
                'Rahul Phukan', 'Jessie Anh Nguyen',
                'Prabhanshu Attri', 'Mrityunjay Sankhla'
            ],
            number: 20
        },
        {
            skill: 'Machine Learning',
            people: [
                'Ankush Singh Gandhi',
                'Preksha Shetti',
                'Anurag Lal',
                'Prathamesh Sankpal',
                'Vaibhav Arora',
                'Rishi Khandelwal',
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Prabhanshu Attri',
                'Srinjoy Ganguly',
                'Rūta Slavickienė',
                'Subhabrata Mukherjee',
                'Amit Bhushan'
            ],
            number: 14
        },
        {
            skill: 'Software Development',
            people: [
                'Nilutpal Baruah',
                'Oshi Gupta',
                'Akash Chetia',
                'Manbir Singh Marwah',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Vishal Rajput',
                'Srinjoy Ganguly',
                'Vansh Bhardwaj',
                'Abhijit Tripathy'
            ],
            number: 10
        },
        {
            skill: 'Data Structures',
            people: [
                'Sayantan Sikdar', 'Anurag Lal',
                'Sai Kamal', 'Rishi Khandelwal',
                'Ayush khandelwal', 'Akash Chetia',
                'Manbir Singh Marwah', 'Ankit Aggarwal',
                'ARYAN GULATI', 'Vishal Rajput',
                'Jessie Anh Nguyen', 'Srinjoy Ganguly',
                'Shubham Sharma', 'Utkarsh Chourasia',
                'Subhabrata Mukherjee', 'Abhijit Tripathy',
                'Shivang Sharma', 'Vishesh Gupta',
                'Jordan Cohen', 'Sonal Kushwaha'
            ],
            number: 20
        },
        {
            skill: 'Algorithms',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Vishal Rajput',
                'Srinjoy Ganguly',
                'Abhijit Tripathy',
                'Vishesh Gupta',
                'Sonal Kushwaha',
                'Marco Nunes',
                'Tushar Sabhani'
            ],
            number: 10
        },
        {
            skill: 'Mathematics',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Vaibhav Sardar',
                'Srinjoy Ganguly',
                'Sonal Kushwaha',
                'Parth Rastogi'
            ],
            number: 7
        },
        {
            skill: 'Unit Testing',
            people: [
                'Sneh Chauhan',
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Nitish Sharma'
            ],
            number: 6
        },
        {
            skill: 'Test Automation',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Srinjoy Ganguly'
            ],
            number: 4
        },
        {
            skill: 'Data Science',
            people: [
                'Shubham Yadav',
                'Vaibhav Arora',
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Shubhangi Gupta'
            ],
            number: 7
        },
        {
            skill: 'Android Development',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Aditya Sharma'
            ],
            number: 5
        },
        {
            skill: 'Data Analysis',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Srinjoy Ganguly'
            ],
            number: 4
        },
        {
            skill: 'Cloud Computing',
            people: [
                'Mohammed Ameer',
                'Akash Chetia',
                'Amaan Ur Rahman',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Aryan Chauhan'
            ],
            number: 6
        },
        {
            skill: 'Project Management',
            people: [
                'Mohammed Ameer',
                'Akash Chetia',
                'Amaan Ur Rahman',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Aryan Chauhan'
            ],
            number: 6
        },
        {
            skill: 'Continuous Integration',
            people: [
                'Mohammed Ameer',
                'Akash Chetia',
                'Amaan Ur Rahman',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Aryan Chauhan'
            ],
            number: 6
        },
        {
            skill: 'Deep Learning',
            people: [
                'Mohammed Ameer',
                'Akash Chetia',
                'Amaan Ur Rahman',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Aryan Chauhan'
            ],
            number: 6
        },
        {
            skill: 'Python',
            people: [
                'Vaibhav Arora',
                'Ajinkya Kale',
                'Surinder Choudhary',
                'Ashish kashyap',
                'Deepak Singh��',
                'Tharun kshathriya',
                'Devesh Anand Srivastava',
                'Rajit Paul',
                'Harsh Koli',
                'Akash Chetia',
                'Tushar R.',
                'Garvitraj Pandey',
                'Kirtan Ghelani',
                'Rahul Choudhary',
                'Rishabh Sachdeva',
                'Abhinav Mishra',
                'Yashas K S',
                'Manbir Singh Marwah',
                'FAIZAN ASHRAF'
            ],
            number: 19
        },
        {
            skill: 'Java',
            people: [
                'Roshan Kumar',
                'Adarsh Sulegai',
                'Monica Chhabria',
                'Harshraj Singh',
                'Ayush Singh',
                'Ayushmaan G.',
                'Ashish kashyap',
                'Devesh Anand Srivastava',
                'Rajit Paul',
                'Tanishq The Creator',
                'Sujit Y.',
                'Akash Chetia',
                'Garvitraj Pandey',
                'Rishabh Sachdeva',
                'Abhinay Parasar',
                'Karan Meena',
                'Abhinav Mishra',
                'Roshan Raut',
                'Yashas K S'
            ],
            number: 19
        },
        {
            skill: 'C++',
            people: [
                'Divyansh Sharma', 'Akash Chetia',
                'Kirtan Ghelani', 'Manbir Singh Marwah',
                'Ankit Aggarwal', 'ARYAN GULATI',
                'Vishal Rajput', 'Srinjoy Ganguly',
                'Abhijit Tripathy', 'T. Jahnavi',
                'Ashish Tiwari', 'Sonal Kushwaha',
                'Pranshul Aggarwal', 'nikhil girdhar',
                'Tushar Sabhani', 'Karan Singh Bora',
                'Marco Nunes', 'Jitmanew T.'
            ],
            number: 18
        },
        {
            skill: 'Docker',
            people: [
                'Akash Chetia',
                'Manbir Singh Marwah',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Sonal Kushwaha'
            ],
            number: 6
        },
        {
            skill: 'Linux',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Vishal Rajput',
                'Srinjoy Ganguly',
                'Utkarsh Chourasia',
                'Sonal Kushwaha'
            ],
            number: 7
        },
        {
            skill: 'JavaScript',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Sonal Kushwaha'
            ],
            number: 5
        },
        {
            skill: 'Node.js',
            people: [
                'Akash Chetia',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Sonal Kushwaha'
            ],
            number: 4
        },
        {
            skill: 'Kotlin',
            people: [
                'Akash Chetia',
                'Roshan Raut',
                'Shivam Kushwaha',
                'ARYAN GULATI',
                'Srinjoy Ganguly'
            ],
            number: 5
        },
        {
            skill: 'Firebase',
            people: [
                'Akash Chetia',
                'Karan Meena',
                'ARYAN GULATI',
                'Srinjoy Ganguly'
            ],
            number: 4
        },
        {
            skill: 'Databases',
            people: [
                'Akash Chetia',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Ashish Tiwari'
            ],
            number: 4
        },
        {
            skill: 'React.js',
            people: ['Akash Chetia', 'ARYAN GULATI', 'Srinjoy Ganguly'],
            number: 3
        },
        {
            skill: 'Microsoft Excel',
            people: ['Akash Chetia', 'ARYAN GULATI', 'Srinjoy Ganguly'],
            number: 3
        },
        {
            skill: 'Google Cloud Platform (GCP)',
            people: [
                'Akash Chetia',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'vineela ampili'
            ],
            number: 4
        },
        {
            skill: 'Microsoft Azure',
            people: ['Akash Chetia', 'ARYAN GULATI', 'Srinjoy Ganguly'],
            number: 3
        },
        {
            skill: 'Prometheus.io',
            people: ['Akash Chetia', 'ARYAN GULATI', 'Srinjoy Ganguly'],
            number: 3
        },
        {
            skill: 'SQL',
            people: ['Akash Chetia', 'ARYAN GULATI'],
            number: 2
        },
        {
            skill: 'Amazon Web Services (AWS)',
            people: ['Akash Chetia', 'ARYAN GULATI'],
            number: 2
        },
        {
            skill: 'MongoDB',
            people: ['Akash Chetia', 'ARYAN GULATI'],
            number: 2
        },
        {
            skill: 'Elasticsearch',
            people: ['Akash Chetia', 'ARYAN GULATI'],
            number: 2
        },
        {
            skill: 'Git',
            people: [
                'Kuyasha Das',
                'Ritik Gupta',
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Vishal Rajput',
                'Vaibhav Sharma',
                'Srinjoy Ganguly',
                'Rūta Slavickienė',
                'Utkarsh Chourasia',
                'Sonal Kushwaha',
                'Marco Nunes',
                'Tushar Sabhani'
            ],
            number: 13
        },
        {
            skill: 'Public Speaking',
            people: [
                'Omar Elsherif',
                'Akash Chetia',
                'Manbir Singh Marwah',
                'ARYAN GULATI',
                'Yajush Vyas',
                'Srinjoy Ganguly',
                'Vansh Bhardwaj',
                'Ritwik Mehta',
                'Sonal Kushwaha'
            ],
            number: 9
        },
        {
            skill: 'Leadership',
            people: [
                'Akash Chetia',
                'Manbir Singh Marwah',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Vansh Bhardwaj',
                'Rūta Slavickienė',
                'Ritwik Mehta'
            ],
            number: 7
        },
        {
            skill: 'Interpersonal Skills',
            people: [
                'Akash Chetia',
                'Manbir Singh Marwah',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Vansh Bhardwaj',
                'Rūta Slavickienė',
                'Ritwik Mehta'
            ],
            number: 7
        },
        {
            skill: 'Teaching',
            people: [
                'Akash Chetia',
                'Manbir Singh Marwah',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Vansh Bhardwaj',
                'Rūta Slavickienė',
                'Ritwik Mehta'
            ],
            number: 7
        },
        {
            skill: 'Kubernetes',
            people: [
                'Akash Chetia',
                'Manbir Singh Marwah',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Sonal Kushwaha'
            ],
            number: 6
        },
        {
            skill: 'Openshift',
            people: ['Akash Chetia', 'ARYAN GULATI', 'Srinjoy Ganguly'],
            number: 3
        },
        {
            skill: 'Web Scraping',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Srinjoy Ganguly',
                'Subhabrata Mukherjee',
                'Ashish Tiwari',
                'Sonal Kushwaha',
                'Tushar Sabhani'
            ],
            number: 8
        },
        {
            skill: 'TypeScript',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Srinjoy Ganguly'
            ],
            number: 4
        },
        {
            skill: 'Go (Programming Language)',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Adesh Khandait',
                'Srinjoy Ganguly'
            ],
            number: 5
        },
        {
            skill: 'Developer Relations',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Adesh Khandait',
                'Srinjoy Ganguly'
            ],
            number: 5
        },
        {
            skill: 'Build Tools',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Adesh Khandait',
                'Srinjoy Ganguly'
            ],
            number: 5
        },
        {
            skill: 'Serverless Computing',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Adesh Khandait',
                'Srinjoy Ganguly'
            ],
            number: 5
        },
        {
            skill: 'Site Reliability Engineering',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Adesh Khandait',
                'Srinjoy Ganguly'
            ],
            number: 5
        },
        {
            skill: 'Full-Stack Development',
            people: [
                'Akash Chetia',
                'Ankit Aggarwal',
                'ARYAN GULATI',
                'Adesh Khandait',
                'Srinjoy Ganguly'
            ],
            number: 5
        }
    ]
    console.log("The Endorsement data is as follows:\n");
    displayEndorsements(endorsements)

    console.log("\n---END---\n")
}

// entry function
init()
