from pathlib import Path
from pickle import load, dump
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from uuid import uuid4
from typing import Dict, List

class EventPlanner:
    def __init__(self, guests: Dict[str, str], schedule: Dict[str, str], topic):
        guests = [{"email": email} for email in guests.values()]
        service = self._authorize()
        self.event_states = self._plan_event(guests, schedule, service, topic)

    @staticmethod
    def _authorize():
        scopes = ["https://www.googleapis.com/auth/calendar"]
        credentials = None
        token_file = Path("./token.pickle")
        if token_file.exists():
            with open(token_file, "rb") as token:
                credentials = load(token)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)
                credentials = flow.run_local_server(port=0)
            with open(token_file, "wb") as token:
                dump(credentials, token)
        calendar_service = build("calendar", "v3", credentials=credentials)
        return calendar_service

    @staticmethod
    def _plan_event(attendees: List[Dict[str, str]], event_time, service: build, topic):
        event = {"summary": topic,
                 "start": {"dateTime": event_time["start"], 'timeZone': 'Asia/Kolkata'},
                 "end": {"dateTime": event_time["end"], 'timeZone': 'Asia/Kolkata'},
                 "attendees": attendees,
                 "conferenceData": {"createRequest": {"requestId": f"{uuid4().hex}", "conferenceSolutionKey": {"type": "hangoutsMeet"}}},
                 "reminders": {"useDefault": True}
                 }
        event = service.events().insert(calendarId="primary", sendNotifications=True, body=event, conferenceDataVersion=1).execute()
        return event

topic = 'Topic of the meeting' # replace with suitable topic
time = {
    'start':'2021-03-25T12:30:00.000000', # replace these with time of meeting
    'end':'2021-03-25T13:00:00.000000'
}
guests = {
    'guest1':'guest1@email.com', # replace these with emails of the guests
    'guest2':'guest2@email.com'
}
meet = EventPlanner(guests, time, topic)
keys = ['organizer','hangoutLink', 'summary', 'start', 'end', 'attendees']
details = { key: meet.event_states[key] for key in keys }
for key in keys:
    print(key+' : ', details[key])
