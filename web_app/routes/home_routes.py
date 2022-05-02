# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template
from web_app.reviewaggregation import fetch_locations
from web_app.review_submit import review_upload

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/homepage")
def index():
    print("You reached the homepage...")
    locations = fetch_locations()
    return render_template("homepage.html", locations=locations)

@home_routes.route("/leaveareview/<int:location_id>")
#@home_routes.route("/leaveareview")
def reviewpage(location_id):
    locations = fetch_locations()
    location_name = locations[location_id-1]["location_name"]
    print("You reached the review page...")
    return render_template("review2.html", location_id=location_id, locations=locations, location_name=location_name)

@home_routes.route("/reviewconfirmation", methods=['GET','POST'])
def confirm():
    print("You submitted a review!")
    form_data = dict(request.form)
    print("FORM DATA:", form_data)
    review_upload(form_data)
    return render_template("confirmation.html")

# ...
