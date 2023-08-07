# 📰 News-Accumulator

A python automation script to quickly gather and view latest happenings and news information from the web</br>
in a summarized and consise way.

### Functionality
First data is scraped from google news to generate list of articles based on the search keyword and publishing agency</br> in tabular manner.
Then data is scraped from the article selected by the user to get the contents from website of that article.
 - Generates a list of relevant articles by title and the respective address based on the given keyword.
 - View the contents of any specified article(Page Contents).
 - Customization options to extract relevant useful pieces of information from the site.

### Technologies Used
- **Requests** for handling web server communicatons and sending get requests
- **Beautiful Soup** for parsing the html of the website and derive useful contents as a dom object
- **xml.dom.minidom** to parse the xml string and store it in a structured way as dom object.

### Requirements
 [Requirement guidelines for this project](requirements.txt)
 
### Running Locally
**It is best to use a python virtual environment**

Create a virtual environment in the project dirctory  env.
```
python -m venv app
```
Activate the virtual environment
```
Windows: app\Scripts\activate
```
Install the required modules `pip install -r requirements.txt`\
Go to the directory containing main.py and type command  `python main.py`

### Usage And Output
Here are some sample run of the program

**Run a new keyword search and get a list of articles**


![alt text](https://i.postimg.cc/Fsdx6LF3/gns1.png)

**Select any article no to view it**

![alt text](https://i.postimg.cc/Y9dx5Nmf/gns2.png)
![alt text](https://i.postimg.cc/FH0VrXLK/gns3.png)

**Menu to perform various actions**
- **Press 2  to view another article**

![alt text](https://i.postimg.cc/xjFRgRQ9/gns4.png)
![alt text](https://i.postimg.cc/hGgbhZL1/gns5.png)

- **Press 3  to search a different set of articles**

![alt text](https://i.postimg.cc/HnjtdJwG/gns6.png)
![alt text](https://i.postimg.cc/kX0yPgDZ/gns7.png)

- **Press 1  to view additional information**

![alt text](https://i.postimg.cc/yd1PppW8/gns8.png)

-   **Press 4  to Exit**
![alt text](https://i.postimg.cc/W4PSg1vr/gns11.png)
