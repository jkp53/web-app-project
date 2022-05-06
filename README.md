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

#the locations and review data is stored on a google sheet at the following [link](https://docs.google.com/spreadsheets/d/1ciNHuyNCIMAYaBFQDNCykwwdWVEZwr2Uo8TnkHcO2Qg/edit#gid=883497855)

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside. These are example contents for the ".env" file:

```sh
# this is the ".env" file... with environment variables
#the google sheet ID can be found in the url of the google sheet that stores the loaction and review data
GOOGLE_SHEET_ID="1ciNHuyNCIMAYaBFQDNCykwwdWVEZwr2Uo8TnkHcO2Qg"
```


Create Google Credentials:

Navigate to [Google Cloud Console](https://console.cloud.google.com) and sign into your account. In the dashboard, create a new project. Then, navigate to "APIs and Services" and search for and the enable the following API'S in the Market Place: "Google Sheets API" and "Google Drive API"

Specicifally manage the Google Drive API by creating your own credentials.

    1. What API are you using? > Google Drive API
    2. Where will you be calling your API from? > Web Server
    3. What data will you be accessing? > Application Data
    4. Select Role > Project > Editor
    5. Key Type > JSON

Move the dowloaded json file into the root directory of this repo. Then rename the file to "google-credentials.json".

## Testing

Run tests:

```sh
pytest
```

## [Deploying](/DEPLOYING.md)

Follow the deployment instructions if you would like to deploy the app on oyur own remote server.

## Server Commands

Run the following code in terminal to run the web app on your local computer:

```sh
FLASK_APP=web_app flask run
#or store the FLASK_APP=web_app in your .env file and then you can just paste 'flask run'
```

Run the following code in terminal to shut down your local server:
```sh
^C
```

## Web App

Visit your web app using the Heroku generated url. To see an example, visit our [Georgetown Campus Dining Reviews Web App](https://dining-location-reviews-app.herokuapp.com/)!


## [License](/LICENSE.md)

Copyright (c) 2015-2022 [John Picker](mailto:jkp53@georgetown.edu).
