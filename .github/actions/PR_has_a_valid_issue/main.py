import os, re, requests

# Used pattern to search for Issues.
pattern = "#\d+"

# PR body
body = os.getenv("INPUT_PRBODY")
# PR URL
url  = os.getenv("INPUT_PRURL")

issue_num = re.search(pattern, body)[0].replace("#", "")

# url list will be something like this
# ['https:', '', 'api.github.com', 'repos', 'owner', 'repo-name']
# Split URL using slashes
url = url.split("/")[:-2]
# Replace API URL with HTML URL
url[2] = url[2].replace("api.", "")
# Get rid of "repos" record
url.pop(3)
# Reattach URL pieces
url = "/".join(url)
# Add issue number
url += "/issues/{}".format(issue_num)

# Is valid code
valid_code = 0
response = requests.get(url)
# Check if not a 404 page
if response.status_code == 200:
    print("status code is 200")
    # Check if not redirected to a pull request page
    if response.url == url:
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
