# epic_games_store_bot [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 
Epic game's weekly free games purchasing bot

Run it on heroku or somewhere

### Process 
```sh
  python trigger.py
  python web.py # To run web ui
```
### Requirements
```sh
gunicorn  # For heroku
requests
flask
selenium
apscheduler
```

# Heroku
 ### Heroku-Buildpacks
  Chrome Driver | https://github.com/heroku/heroku-buildpack-chromedriver 
  --------------|---------------------------------------------------------
  Chrome Binary | https://github.com/heroku/heroku-buildpack-google-chrome
 
 ### Heroku-Procfile
  ```sh
  Procfile
     web: gunicorn web:app
     worker: python trigger.py
  ```

License
----

MIT
