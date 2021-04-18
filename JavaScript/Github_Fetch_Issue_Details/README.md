
# Issue Fetch Script

#### Its a script to capture the following points:
- Issue Creator
- Issue Assignee
- Issue Open/Close Date
- People who commented on the Issue (Numbers and their Username)
- Issue Content


## Setup instructions
- Create a .env file and put the Authorization variable as:
  - `Authorization = <Your Github Personal Token>`

- Now put your username and the repository you wanna test on lines 67 and 68 in issueDetails.js.Now, you are good to go and use the following script.

## Detailed explanation of script, if needed
Script could be understood in a following manner:
- Primarily there is a function `getDetails` in which username and repoName is passed.
- First all the issues is obtained from that repository.
- After that that array of issues is mapped to get all the details.

## Output

https://user-images.githubusercontent.com/63748249/115146968-856c8980-a076-11eb-96c1-86a2dbc24c93.mp4

## Author
#### Naman

