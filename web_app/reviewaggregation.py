

import gspread
import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
#from web_app.locations import locations
import pandas as pd

load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="1ciNHuyNCIMAYaBFQDNCykwwdWVEZwr2Uo8TnkHcO2Qg")

# an OS-agnostic (Windows-safe) way to reference the "auth/google-credentials.json" filepath:
CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__),"..", "google-credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

def fetch_locations():
    """
This function connects to the google sheet in the backend and fetches all the locations and review data
from the google sheet. It then calculatees the overall score for each review for every location and
averages them to get each location's rating. The user doesn't have to invoke this function.
It is called automatically when the homepage is loaded. It also is called when a user clicks to leave a review, because the locations need
to be fetched to pull the name of the selected See the home_routes.py file to see where it is used.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
    client = gspread.authorize(credentials)
    doc = client.open_by_key(DOCUMENT_ID)

    locations_sheet = doc.worksheet("dining_locations")
    locations = locations_sheet.get_all_records()
    reviews_sheet = doc.worksheet("dining_reviews")
    reviews = reviews_sheet.get_all_records()

    for location in locations:
        overall_score_list = []
        for review in range (0, len(reviews)):
            if reviews[review]["location_id"]==location["location_id"]:
                overall_review_score = (reviews[review]["taste_score"]+reviews[review]["health_score"]+reviews[review]["service_score"]+reviews[review]["portion_score"])/4
                overall_score_list.append(overall_review_score)
        average_overall_score = round(sum(overall_score_list)/len(overall_score_list),1)
        location.update(rating=average_overall_score)


    return locations
    #print(locations)
