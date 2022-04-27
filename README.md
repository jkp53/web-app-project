# web-app-project


## Installation

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

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# these are example contents for the ".env" file:


# optional vars:
#APP_ENV="development"
#COUNTRY_CODE="US"
#ZIP_CODE="10017"
#USER_NAME="Jon Snow"
```

## Usage

Printing today's weather forecast (to test the Weather.gov API):

```sh
python -m app.weather_service

# in production mode:
APP_ENV="production" COUNTRY_CODE="US" ZIP_CODE="20057" python -m app.weather_service
```


## Testing
## [Deploying](/DEPLOYING.md)

Follow the deployment instructions to deploy the app to a remote server and schedule the server to send you the weather forecast email every day.


## [License](/LICENSE.md)

## Web App Commands

run the following code in terminal:
```sh
FLASK_APP=web_app flask run
#or store the FLASK_APP=web_app in your .env file and then you can just paste 'flask run'
```
