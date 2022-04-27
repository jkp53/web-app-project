# Reading csv from google sheets

# Code adapted from https://www.youtube.com/watch?v=cnPlKLEGR7E

import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS, PLEASE SET Google Sheet ID")
SHEET_NAME = os.getenv("LOCATIONS_SHEET_NAME", default="dining_locations")

# an OS-agnostic (Windows-safe) way to reference the "auth/google-credentials.json" filepath:
CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__),"..", "auth", "google-credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
#print("CREDS:", type(credentials)) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>

client = gspread.authorize(credentials)

doc = client.open_by_key(DOCUMENT_ID)
sheet = doc.worksheet(SHEET_NAME)

locations = sheet.get_all_records()
