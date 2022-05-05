# Web App Project

A Completed Repository for the [The Self-Directed "Freestyle" Project](https://github.com/prof-rossetti/intro-to-python/tree/main/projects/freestyle).

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Optionally fork this [remote repository](https://github.com/jkp53/web-app-project), to create a copy under your own control. Then "clone" or download the remote repository (or your forked copy) onto your local computer, for example to your Desktop. Then navigate to wherever you downloaded the repo:

```sh
cd ~/Desktop/python/web-app-project
```

Use Anaconda to create and activate a new virtual environment, perhaps called "briefings-env":

```sh
conda create -n dining-reviews-env python=3.8
conda activate dining-reviews-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate. These are example contents for the ".env" file:

```sh
# this is the ".env" file... with environment variables

#this is your google sheet specific API key in the url
DOCUMENT_ID="________"
```


Create Google Credentials:

Navigate to [Google Cloud Console](https://console.cloud.google.com) and sign into your account. In the dashboard, create a new project. Then, navigate to "APIs and Services" and search for and the enable the following API'S in the Market Place: "Google Sheets API" and "Google Drive API"

Specicifally manage the Google Drive API by creating your own credentials. 

    1. What API are you using? > Google Drive API
    2. Where will you be calling your API from? > Web Server
    3. What data will you be accessing? > Application Data
    4. Select Role > Project > Editor
    5. Key Type > JSON

Move the dowloaded json file into the root directory of this repo and replace the json file name in the following python files: "review_submit.py" and "reviewaggregation.py". The change occurs in the following line of code:

```sh
CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__),"..", "google-credentials.json")
```

Finally, navigate to your google sheet, change share settings to "Anyone with the link", and share the document with the generated "client_email" found within the downloaded json file.


Google Sheets Format:

Create two sheets named, "dining_locations" and "dining reviews".

Within the "dining_locations" sheet add the following column headers: "location_id", "location_name", "location_hours", "location_logo_url"
Within the "dining_reviews" sheet add the following column headers: "location_id", "taste_score", "health_score", "service_score", "portion_score"

Input desired variables in each column.

## Testing

Run tests:

```sh
pytest
```

## [Deploying](/DEPLOYING.md)

Follow the deployment instructions to deploy the app to a remote server.

Specifically when configuring the server on heroku, include the following environment variables:

```sh
DOCUMENT_ID="______"
#google sheet API key found in the url
```

```sh
CREDENTIALS_FILEPATH="_______"
#copy and paste all the contents found within your downloaded json file
```

## Server Commands

Run the following code in terminal to start your server:

```sh
FLASK_APP=web_app flask run
#or store the FLASK_APP=web_app in your .env file and then you can just paste 'flask run'
```

Run the following code in terminal to shut down your server:
```sh
^C
```

## Web App

Visit your web app using the Heroku generated url. To see an example, visit our [Georgetown Campus Dining Reviews Web App](https://dining-location-reviews-app.herokuapp.com/)!


## [License](/LICENSE.md)

Copyright (c) 2015-2022 [John Picker](mailto:jkp53@georgetown.edu).
