# Reading csv from google sheets

# Code adapted from https://www.youtube.com/watch?v=cnPlKLEGR7E

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('web_app/gu-dining-locations-cf538c00daae.json', scope)

client = gspread.authorize(creds)

workbook1 = client.open("Georgetown Dining Locations Data").sheet1

locations = workbook1.get_all_records()

print(locations)
