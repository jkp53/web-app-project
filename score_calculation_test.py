from web_app.reviewaggregation import fetch_locations

def test_score_calc():

    assert len(fetch_locations()) == 14
