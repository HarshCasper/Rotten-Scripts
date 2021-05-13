### Subdomain Finder

This Script is used to find the possible subdomains of a domain.

### Domain name

The url format for a domain name is: "http://subdomain.domain.top-level-domain"

### Setup

1. Create a Virtual Environment.
2. Install the requirements by using `pip3 install -r requiremnts.txt`
3. Hurray.! You're ready to use the Script.

### Prerequisites

1. The available_subdomains.txt should be in the current directory whre the program exists. 
2. If you want to use your own file place it in the current directory where the program exists.

### Running a file

1. Run the script using `python3 subdomain_finder.py`

2. When asked for domain, enter `your domain` . For example: wiki.com

3. When asked for size, enter `size` . For example: 10 [Max-1000] 

3. While the program is working you can view in the terminal:
    + means a possible subdomain is found
    . means the subdomain is not available

### Sample Test Case

Enter `wiki.com` when asked for input domain.

Run the script and observe that output.csv file is created and it contains the possible subdomains.

#### All the requirements for this script is mentioned in **requirements.txt** file.