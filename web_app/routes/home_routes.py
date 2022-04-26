# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template, redirect

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/homepage")
def index():
    print("You reached the homepage...")
    locations = [
        {"location_id":"1", "location_name":"Five Spice", "location_hours":"hours test", "location_logo_url":"https://cms.concept3d.com/map/lib/image-cache/i.php?mapId=999&image=999/Logos-bgTransparent_5Spice.png&w=900&h=508&r=1"},
        {"location_id":"2", "location_name":"Olive Branch", "location_hours":"Monday – Thursday 11:00am – 8:00pm; Friday 11:00am – 4:00pm; Sunday 4:00pm – 8:00pm", "location_logo_url":"https://cms.concept3d.com/map/lib/image-cache/i.php?mapId=999&image=999/Logos-bgTransparent_OliveBranch.png&w=900&h=508&r=1"},
        {"location_id":"3", "location_name":"Whisk", "location_hours":"hours test", "location_logo_url":"https://cms.concept3d.com/map/lib/image-cache/i.php?mapId=999&image=999/Logos-bgTransparent_Whisk.png&w=900&h=508&r=1"}
        ]

    print(type(locations))
    return render_template("homepage.html", locations=locations)

@home_routes.route("/leaveareview/<int:location_id>")
#@home_routes.route("/leaveareview")
def reviewpage(location_id):
    print("You reached the review page...")
    print("You chose location " + str(location_id))
    return render_template("review2.html", location_id=location_id)

@home_routes.route("/reviewconfirmation", methods=["POST"])
def confirm():
    print("You submitted a review!")
    form_data = dict(request.form)
    print("FORM DATA:", form_data)
    return redirect("/")


    # web_app/routes/home_routes.py

# ...
