import requests

# Change the file name as per requirements.
#
with open('pagespeed.txt') as pagespeedurls:
    download_dir = 'pagespeed-results.csv'
    # Start writing the CSV file
    file = open(download_dir, 'w')
    content = pagespeedurls.readlines()
    content = [line.rstrip('\n') for line in content]
    # Populate Columns
    columnTitleRow = "URL, First Contentful Paint, First Interactive\n"
    file.write(columnTitleRow)

    # For loop for reading separate URLs from text file.
    for line in content:
        # Merging the Url from text file in order to successfully request from API
        # Strategy is an optional argument
        # It can be-
        """
        "desktop": Fetch and analyze the URL for desktop browsers
        "mobile": Fetch and analyze the URL for mobile devices
        """
        api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}&strategy=desktop'
        print(f'Requesting {api_url}...')
        r = requests.get(api_url)
        final = r.json()

        try:
            url_ID = final['id']
            # This splits the absolute url from the api key parameter
            split = url_ID.split('?')
            # This reassigns url_ID to the absolute url
            url_ID = split[0]
            ID = f'URL ~ {url_ID}'
            ID2 = str(url_ID)
            urlfcp = final['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
            FCP = f'First Contentful Paint ~ {str(urlfcp)}'
            FCP2 = str(urlfcp)
            urlfi = final['lighthouseResult']['audits']['interactive']['displayValue']
            FI = f'First Interactive ~ {str(urlfi)}'
            FI2 = str(urlfi)
        except KeyError:
            print(f'<KeyError> One or more keys not found {line}.')

        try:
            row = f'{ID2},{FCP2},{FI2}\n'
            file.write(row)
        except NameError:
            print(f'NameError in {line}.')
            file.write(
                f'Failing because of inconsistent key in {line}.' + '\n')

        try:
            print(ID)
            print(FCP)
            print(FI)
        except NameError:
            print(f'KeyError in {line}.')

    file.close()
