'''
This gist is generated by Python.
'''
#!/usr/bin/env python

import requests
import json

GITHUB_API = "https://api.github.com"
API_TOKEN = 'your-token-goes-here'

# form a request URL
url = GITHUB_API+"/gists"
print("Request URL: %s" % url)

# print headers,parameters,payload
headers = {'Authorization': 'token %s' % API_TOKEN}
params = {'scope': 'gist'}
payload = {"description": "GIST created by python code", "public": True, "files": {
    "Gist by Python": {"content": "This gist is created by Python."}}}

# make a requests
res = requests.post(url, headers=headers, params=params,
                    data=json.dumps(payload))

# print response --> JSON
print(res.status_code)
print(res.url)
print(res.text)
j = json.loads(res.text)

# Print created GIST's details
for gist in range(len(j)):
    print("Gist URL : %s" % (j['url']))
    print("GIST ID: %s" % (j['id']))
