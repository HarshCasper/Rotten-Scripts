>## SUBDOMAIN FINDER

<p>This Script is used to find the possible subdomains of a domain. The basic principle behind this is 
Brute Force Checking if a URL can exist or not. From a list of subdomains, we generate a URL for each.
Then using a HTTP request we check if a connection can be established. If yes it is a possible subdomain otherwise not.</p>

---
## Domain name

The URL format for a domain name is: _`http://subdomain.domain.top-level-domain`_

---
## Dependencies
<p>The dependencies for this Script are as follows. </p>

* requests==2.25.1
* virtualenv==20.3.0

<p>For installation follow the steps in Setup below.<p>

---
## Setup
1. Change working directory to the current directory 
```bash
cd Python/Subdomain_Finder
```

2. Install the requirements by using the following command. Skip if already installed.

```bash
pip3 install -r requiremnts.txt
```

3. Create a Virtual Environment.
```bash
virtualenv myvenv -p python3
```

4. Activating the Virtual Environment.
```cmd
myvenv\Scripts\activate
```

5. To deactivate the Virtual Environment.
```cmd
deactivate
```
---
## Prerequisites

1. The [available_subdomains.txt](../Subdomain_Finder/available_subdomains.txt "subdomains file") should be in the current directory whre the program exists. 
2. If you want to use your own file place it in the current directory where the program exists.

---
## Running the Script

1. Run the script using 
```python
python3 subdomain_finder.py
```

2. When asked for domain, enter your domain.
```text
your domain
```

3. When asked for size enter size(Maximum-1000).  
```text
size
```

4. While the program is working you can view in the terminal:
    * <p>+ (plus) means a possible subdomain is found.</p>
    * <p>. (period) means the subdomain is not available.</p>

>## Example

1. Change working directory to the current directory 
```bash
cd Python/Subdomain_Finder
```

2. Run the script using 
```python
python3 subdomain_finder.py
```

3. When asked for domain, enter your domain.
```text
wiki.com
```

4. When asked for size enter size(Maximum-1000).  
```text
10
```

5. A csv file is created in the current directory with name [output.csv](../Subdomain_Finder/output.csv "output file").

---
## Author

[Tanishq Arya](https://github.com/tanishq-arya "Github profile link")

<p>Worked on the script under GirlScript Summer of Code 2021.<br> Click on name to view github profile.</p>

