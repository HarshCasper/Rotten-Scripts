from googleapiclient.discovery import build
import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]


def main():
    url = input("Enter the path of folder or file:- ")
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("drive", "v3", credentials=creds)

    # If path is for folder
    if "folders" in url.split("/"):
        folder_id = url.split("folders/")[1].split("/")[0].split("?")[0]
        folder_name = input("Enter name of folder:- ")
        print(folder_id)
        download_folder(service, folder_id, "./", folder_name)
    # If path is for file
    else:
        file_id = url.split("/d/")[1].split("/")[0].split("?")[0]
        file_service = service.files()
        file_name = file_service.get(fileId=file_id, fields="*").execute()["name"]
        download_file_from_google_drive(file_id, "./" + file_name)


def download_folder(service, folder_id, location, folder_name):

    if not os.path.exists(location + folder_name):
        os.makedirs(location + folder_name)
    location += folder_name + "/"

    result = []
    page_token = None
    while True:
        files = (
            service.files()
            .list(
                q="'{}' in parents".format(folder_id),
                fields="nextPageToken, files(id, name, mimeType, shortcutDetails)",
                pageToken=page_token,
                pageSize=1000,
            )
            .execute()
        )
        result.extend(files["files"])
        page_token = files.get("nextPageToken")
        if not page_token:
            break

    result = sorted(result, key=lambda k: k["name"])

    total = len(result)
    current = 1
    for item in result:
        file_id = item["id"]
        filename = item["name"]
        mime_type = item["mimeType"]
        shortcut_details = item.get("shortcutDetails", None)
        if shortcut_details is not None:
            file_id = shortcut_details["targetId"]
            mime_type = shortcut_details["targetMimeType"]
        print(filename, mime_type, "({}/{})".format(current, total))
        if mime_type == "application/vnd.google-apps.folder":
            download_folder(service, file_id, location, filename)
        elif not os.path.isfile(location + filename):
            download_file_from_google_drive(file_id, location + filename)
        current += 1


def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith("download_warning"):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={"id": id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {"id": id, "confirm": token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


if __name__ == "__main__":
    main()
