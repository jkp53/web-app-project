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

First, you will need to create and download Google API credentials. To do so, follow the instructions below:

Visit the [Google Developer Console](https://console.developers.google.com/cloud-resource-manager). Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" and enable it. Also search for the "Google Drive API" and enable it.

From either API page, or from the [API Credentials](https://console.developers.google.com/apis/credentials) page, follow a process to create and download credentials to use the APIs:
  1. Click "Create Credentials" for a "Service Account". Follow the prompt to create a new service account named something like "spreadsheet-service", and add a role of "Editor".
  2. Click on the newly created service account from the "Service Accounts" section, and click "Add Key" to create a new "JSON" credentials file for that service account. Download the resulting .json file (this might happen automatically).
  3. Rename the file "google-credentials.json". Then move a copy of the credentials file into your project repository.

Ensure that your repository's '.gitignore' file contains the following code so that your personal credentials do not get tracked in version control or uploaded to GitHub:

```sh
google-credentials.json
*.json
```

Next, create a '.env' file in your project repository. You should create a new environment variable called `GOOGLE_SHEET_ID` and set it equal to `"1ciNHuyNCIMAYaBFQDNCykwwdWVEZwr2Uo8TnkHcO2Qg"`.

Your '.env' file should look something like this:
```sh
GOOGLE_SHEET_ID="1ciNHuyNCIMAYaBFQDNCykwwdWVEZwr2Uo8TnkHcO2Qg"
```

Add `.env` and `__pycache__` to your `.gitignore` file if they are not there already. Save your .env and .gitignore files.

Your '.gitignore' file should now look something like this:
```sh
google-credentials.json
*.json
.env
__pycache__
```

FYI, the locations and review data is stored on a google sheet at the following [link](https://docs.google.com/spreadsheets/d/1ciNHuyNCIMAYaBFQDNCykwwdWVEZwr2Uo8TnkHcO2Qg/edit#gid=883497855). If you want to have your own data imitating the template we have linked above, with the same sheet names and column headers.

## Testing

Run tests:

```sh
pytest
```

## [Deploying](/DEPLOYING.md)

Follow the deployment instructions if you would like to deploy the app on your own remote server.

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
