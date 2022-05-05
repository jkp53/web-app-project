# This is the "review_test.py" file..

from web_app.review_submit import review_upload

def test_if_new_row_created_for_review():

    #this tests whether a user submission is inserted correctly into the data sheet (check for one inserted row)
    form_data_test = {"location_id":"1", "taste_score":"3", "health_score":"3", "service_score":"3","portion_score":"3"}
    assert review_upload(form_data_test) == 1
