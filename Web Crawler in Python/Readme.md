# Web Crawler in Python

## Description
A web crawler is an automated program script that browses the world-wide-web and it can look and store the contents of the web page. This process is called web crawling. Libraries such as BeauitfulSoup, requests parsing a web page in a very simple manner. The search engines like Google use this technique to find up-to-date information. 
- We can use the multi-threading concept. 


### Language
- [X] Python

### Checklist
Name | About
:------------------ | :------------------
Web Crawler |  Automated program script that browses the world-wide-web and it can look and store the contents of the web page.

### Installation
```bash
$ pip install requests
$ pip install bs4
``` 

### Usage
To access the `web crawler`, this application imports the following modules.
```python
import requests
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
```

### Instructions to run this application

  1.  Download the code from  __web_crawler.py__.
  2.  Run the program.
  3. It will give the list of URLs of a particular website. 
