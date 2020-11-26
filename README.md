# epic_games_store_bot [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 
Epic game's weekly free games purchasing bot

App scheduled to run everyday @ 12:00 (timezone changes with system timezone)
if you want to change time

edit trigger.py hour=#any_hour (0 - 24)
```python
16   sched.add_job(trigg, 'cron', day_of_week='mon-sun', hour=12) # Runs everyday @ 12:00 
```

Run it on heroku or somewhere or to run locally without scheduling run web.py and run from there.

---
### Process 
You can run web.py and run whole program without scheduling it'll purchase everything available at that time.
the default username & password is 'admin' & '123'

web.py
```python
36        if username == 'admin' and password == '123':       # change it if you want to.
```

To run.
```sh
  python web.py # To run web-panel
```
### Requirements
```sh
gunicorn  # For heroku
requests
flask
selenium
apscheduler
```
---
# Heroku
Use files included in [Heroku-Files/](https://github.com/5H4D0W-C0D3R/epic_games_store_bot/tree/master/Heroku-Files)
```sh
    Heroku-Files
    ├── Procfile
    └── runtime.txt
```
 ### Steps to Deployment 
  **Step 1** : Create a new account for [Heroku](https://signup.heroku.com/)
  
  **Step 2** : Download Heroku [CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) and [Git](https://git-scm.com/downloads)
                    
    # Setup git
    $ git config --global user.name "#your_name"
    $ git config --global user.email #your_email
  
  **Step 3** :  
  ```sh
    $ heroku create #your_appname
    $ heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-chromedriver -a #your_appname
    $ heroku buildpacks:add --index 2 https://github.com/heroku/heroku-buildpack-google-chrome -a #your_appname
    $ git clone https://github.com/5H4D0W-C0D3R/epic_games_store_bot.git #your_appname
    $ cd #your_appname
    $ rm -rfv .git
    $ mv -v Heroku-Files/* .
  ```
   
  **Step 4** : 
  ```sh
    $ git init
    $ git add -A
    $ git commit -am "#your_appname"
    $ git push heroku master
  ```
  
  **Step 5** : Your app will be deployed to http://#your_appname.herokuapp.com/ go there to access web-panel (web.py)
  
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
---
License
----

MIT
