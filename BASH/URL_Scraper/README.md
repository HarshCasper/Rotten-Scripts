# Extract URL(s) from a web page

[![Bash Shell](https://img.shields.io/static/v1?label=MADE%20WITH&message=BASH&color=red&style=for-the-badge&logo=gnu-bash)](https://shields.io/)
[![Linux](https://img.shields.io/static/v1?label=MADE%20FOR&message=LINUX&color=red&style=for-the-badge&logo=linux)](https://shields.io/)

Bash scripting is very powerful and can be used to perform difficult tasks as web scraping too. In general `grep` is a popular tools for finding text in a file and so many other applications. Combined with other tools like `lynx`, `sed, `awk` and `curl`, bash script can be used to extract url from a web page directly from the terminal.

## Prerequisite

You must have `lynx` and `curl` installed in order to use this script. Check using command given below. This will check as well as install the packages.

```bash
    sudo apt-get update && sudo apt-get install -y lynx curl
```
All other packages comes pre-installed in most linux distributions. In case of an error, install that package.

## Usage

- Download [url_scraper.sh](url_scraper.sh) file, or copy the content of this file to a local file on your system.

- Goto the folder and run the script

```bash
    # without any argument
    ./url_scraper.sh
    # output
    Usage: ./url_scraper.sh [-d|-r|-a] url
        -d      list primary domains of every link
        -r      list only relative links to site
        -a      list all links
```

## Output

- With URL as argument ( same as ./url_scraper.sh -a www.google.com)
```bash
    ./url_scraper.sh www.google.com
    # output
    http://maps.google.co.in/maps
    http://www.google.co.in/history/optout
    http://www.google.co.in/imghp
    http://www.google.co.in/services/
    http://www.google.com/advanced_search
    http://www.google.com/intl/en/about.html
    http://www.google.com/intl/en/ads/
    http://www.google.com/intl/en/policies/privacy/
    http://www.google.com/intl/en/policies/terms/
    http://www.google.com/preferences
    http://www.google.com/setprefdomain
    http://www.google.com/setprefs
    http://www.youtube.com/
    https://accounts.google.com/ServiceLogin
    https://drive.google.com/
    https://mail.google.com/mail/
    https://news.google.com/
    https://play.google.com/
    https://www.google.co.in/intl/en/about/products
    [found 19 url(s): 9 OK | 10 Redirected | 0 Broken]
```

- With -d flag and URL argument

```bash
    ./url_scraper -d www.google.com
    # output
    accounts.google.com
    drive.google.com
    mail.google.com
    maps.google.co.in
    news.google.com
    play.google.com
    www.google.co.in
    www.google.com
    www.youtube.com
    [found 9 domain(s): 2 OK | 7 Redirected | 0 Broken]
```

- With -r flag and URL argument

```bash
    ./url_scrapper -r www.google.co.in
    # output
    intl/en/about/products
    [found 1 relative url(s): 0 OK | 1 Redirected | 0 Broken]
```

## Author(s)

Created by [Avinal Kumar](https://github.com/avinal)
