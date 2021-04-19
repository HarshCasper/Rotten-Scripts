import os, re, requests

pattern = "#\d+"  # Used pattern to search for Issues.

body = os.getenv("INPUT_PRBODY")  # PR body
url  = os.getenv("INPUT_PRURL")   # PR URL

issue_num = re.search(pattern, body)[0].replace("#", "")

# url list will be something like this
# ['https:', '', 'api.github.com', 'repos', 'owner', 'repo-name']
url = url.split("/")[:-2]               # Split URL using slashes
url[2] = url[2].replace("api.", "")     # Replace API URL with HTML URL
url.pop(3)                              # Get rid of "repos" record
url = "/".join(url)                     # Reattach URL pieces
url += "/issues/{}".format(issue_num)   # Add issue number

valid_code = 0                          # Is valid code
response = requests.get(url)
if response.status_code == 200:         # Check if not a 404 page
    print("status code is 200")
    if response.url == url:             # Check if not redirected to a pull request page
        print("URLS are matched")
        # Check if Issue is Open not Closed
        text = response.text
        pattern_issue = "Status:\s(\w+)"
        if re.search(pattern_issue, text)[1] == "Open":
            valid_code = 1
        else:
            print("Couldn't find Open flag")
else:
    print("Invalid Response Code obtained - error code: {}".format(response.status_code))

print("Valid flag is:", valid_code)

print(f"::set-output name=valid::{valid_code}")
        
        
