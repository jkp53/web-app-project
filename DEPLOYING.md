# Deploying to Heroku

## Prerequisites

If you haven't yet done so, [sign up for a Heroku account](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/heroku.md#prerequisites) and [install the Heroku CLI](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/heroku.md#installation), and make sure you can login and list your applications.

```sh
heroku login # just a one-time thing when you use heroku for the first time

heroku apps # at this time, results might be empty-ish
```

> NOTE: some students have reported that when running `heroku login` in Git Bash, it hangs after successfully logging them in. If this is the case for you, close that Git Bash window and when you open a new one you should be all set.

## Server Setup

> IMPORTANT: run the following commands from the root directory of your repository!

Use the online [Heroku Dashboard](https://dashboard.heroku.com/) or the command-line (instructions below) to [create a new application server](https://dashboard.heroku.com/new-app), specifying a unique name (e.g. "notification-app-123", but yours will need to be different):

```sh
heroku create notification-app-123 # choose your own unique name!
```

Verify the app has been created:

```sh
heroku apps
```

Also verify this step has associated the local repo with a remote address called "heroku":

```sh
git remote -v
```


## Server Configuration

Before we copy the source code to the remote server, we need to configure the server's environment in a similar way we configured our local environment.

Instead of using a ".env" file, we will directly configure the server's environment variables by either clicking "Reveal Config Vars" from the "Settings" tab in your application's Heroku dashboard, or from the command line (instructions below):

![a screenshot of setting env vars via the app's online dashboard](https://user-images.githubusercontent.com/1328807/54229588-f249e880-44da-11e9-920a-b11d4c210a99.png)

```sh
# or, alternatively...

# get environment variables:
heroku config # at this time, results might be empty-ish

# set environment variables:

#set APP environment variable to production
heroku config:set APP_ENV="production"

#this is the same thing that you set for your .env file
heroku config:set GOOGLE_SHEET_ID = "_________"

#you will need to copy the entire contents from your google-credentials.json file and paste them to configure the GOOGLE_CREDENTIALS environment variable
heroku config:set GOOGLE_CREDENTIALS = "_______"


```
At this point, you should be able to verify the production environment has been configured with the proper environment variable values:

```sh
heroku config
```

Now login to heroku on the web and go to your project. First, on the Overview tab under 'Dyno formation', you want to add the following code: `gunicorn "web_app:create_app()"`. Next, navigate to the Settings tab and  find buildpacks. You will need to add two buildpacks for the app to run properly. Add the `heroku/python` buildpack and then add another buildpack by pasting the following url: `https://github.com/s2t2/heroku-google-application-credentials-buildpack`


## Deploying

After this configuration process is complete, you are finally ready to "deploy" the application's source code to the Heroku server:
(Note: Make sure you have committed and pushed to Github before doing this for the first time.)

```sh
git push heroku main
```

> NOTE: any time you update your source code, you can repeat this deployment command to upload your new code onto the server

## Viewing your Web App on the Heroku server
After you push your code to the heroku server, you will see near the bottom of a line of code that looks something like:

```sh
remote: https://dining-location-reviews-app.herokuapp.com/ deployed to Heroku
```
The url is where your web app lives on the internet. Feel free to cpy and paste this in the browser of your choice to view your web app which is now live on the internet!
