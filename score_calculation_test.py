from web_app.reviewaggregation import fetch_locations

#this tests whether the function fetch_locations is working
# properly and pulling the right amount of locations from the google sheet in
def test_score_calc():

    #this tests whether 14 dictionaries have been fetched (one for each location)
    assert len(fetch_locations()) == 14

    #this tests whether the location dictionaries are fetched properly
    first_location = fetch_locations()[0]
    assert first_location["location_name"] == "Downstairs Leos"

    #this tests whether there are five key value pairs in each dictionary
    number_of_dict_pairs = len(first_location)
    assert number_of_dict_pairs == 5
