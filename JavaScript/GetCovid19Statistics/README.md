# Script to retrieve COVID-19 stats using country name
## Description
The script provides live Covid-19 statistics of a country by using "covid19-stats", an NPM module to retrieve worldometer's live Covid-19 stats. The module uses web scraping to obtain real time access to world wide statistical information. Using this script, you can provide the country name as input and get a JsonArray containing latest statistics of the desired country (as listed in worldometers) such as: country, totalCases, newCases, totalDeaths and newDeaths.

## Inputs

**country *Text***

Country name as text input.


## Outputs

**covid19StatsReport *JsonArray***

Covid-19 statistics report as per the country provided as input.

# Usage

- Clone the folder.
- Open command line and change the directory to your folder by using `cd foldername`
- Run the command `npm intall` to import all required modules.
- If you still face module import error, try using `npm install package-name` to install missing modules.
- then run the script by using the command `node index.js`.

this script is meant for educational purposes only.

# Demo
![Screenshot (330)](https://user-images.githubusercontent.com/80174214/160258324-d09bb350-6cc5-4f41-bead-6e9dbf5373f5.png)
