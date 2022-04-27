# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template
from web_app.reviewaggregation import locations
from web_app.review_submit import review_upload

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/homepage")
def index():
    print("You reached the homepage...")
    return render_template("homepage.html", locations=locations)

@home_routes.route("/leaveareview/<int:location_id>")
#@home_routes.route("/leaveareview")
def reviewpage(location_id):
    print("You reached the review page...")
    #for location in locations:
    #    if location["location_id"] == str(location_id):
    #        #location_name == location["location_name"]
    #        print("You chose to review " + location["location_name"])
    return render_template("review2.html", location_id=location_id)

@home_routes.route("/reviewconfirmation", methods=['GET','POST'])
def confirm():
    print("You submitted a review!")
    form_data = dict(request.form)
    print("FORM DATA:", form_data)
    review_upload(form_data)
    return render_template("confirmation.html")


    # web_app/routes/home_routes.py

# ...
