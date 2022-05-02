def review_upload(form_data):

    """
This function connects to the google sheet in the backend and then appends/stores the user's review score inputs
in a new row onto the google sheet. The user doesn't have to invoke this function. It is called automatically
when the user clicks submit on the review 2 page. See the home_routes.py file to see where it is used.
    """

    import gspread
    import os
    from dotenv import load_dotenv
    from oauth2client.service_account import ServiceAccountCredentials
    from pprint import pprint
    #from web_app.locations import locations
    import pandas as pd

    load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

    DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS, PLEASE SET Google Sheet ID")
    SHEET_NAME = os.getenv("REVIEWS_SHEET_NAME", default="dining_reviews")

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

    new_reviews = list(form_data.values())
    integer_reviews = list(map(int, new_reviews))
    sheet.insert_row(integer_reviews,2)
