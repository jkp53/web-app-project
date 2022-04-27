# Reading csv from google sheets

# Google sheets import code adapted from https://www.youtube.com/watch?v=cnPlKLEGR7E

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from locations import locations

import pandas as pd

scope2 = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds2 = ServiceAccountCredentials.from_json_keyfile_name('web_app/gu-dining-locations-cf538c00daae.json', scope2)

client2 = gspread.authorize(creds2)

workbook2 = client2.open("Georgetown Dining Reviews Data").sheet1

# List of dictionaries (all values corresponsing to the csv file)
data2 = workbook2.get_all_records()

average_score_list = []
for location in locations:
    overall_score_list = []
    for review in range (0, len(data2)):
        if data2[review]["location_id"]==location["location_id"]:
            overall_review_score = (data2[review]["taste_score"]+data2[review]["health_score"]+data2[review]["service_score"]+data2[review]["portion_score"])/4
            overall_score_list.append(overall_review_score)
    average_overall_score = sum(overall_score_list)/len(overall_score_list)
    average_score_list.append(average_overall_score)
print(average_score_list)
