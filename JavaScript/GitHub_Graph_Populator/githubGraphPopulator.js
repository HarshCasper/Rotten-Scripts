// Required packages
const jsonfile = require('jsonfile');
const moment = require('moment');
const simpleGit = require('simple-git');
const random = require('random');

// Path of data file(used to make changes for creating fake commits)
const FILE_PATH = './data.json';

const makeCommit = n => {
    if(n===0) return simpleGit().push();
    const week_num = random.int(0,54);
    const day_num = random.int(0,6);
    const DATE = moment().subtract(1,'y').add(1,'d').add(week_num,'w').add(day_num,'d').format();       // Manipulation of Date
    const data = {
        date: DATE
    }
    console.log("New commit made on " + DATE);      // Log dates to your console on which fake commits are made
    jsonfile.writeFile(FILE_PATH, data, ()=>{
        simpleGit().add([FILE_PATH]).commit(DATE, {'--date': DATE},
        makeCommit.bind(this, --n));
    });
}
makeCommit(100);        // Argument Value = Number of fake commits to be made