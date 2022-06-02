
# Bank Security Console

Simple django-based security console.

Main funcionality:
- Shows active pass cards of staff with registration date
- Shows all current visits in storage with duaration
- Shows all visits by person with duration and suspicious flag

## How to install

Python3 should be already installed.

Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

.env variables are used for security purposes in this project.

To setup them you should create .env file in your settings.py directory
and define all personal database and secret key options of your porject in environment (.env) file.
For example:
```
PORT = 8000
```
More information about [dotenv lib](https://pypi.org/project/python-dotenv/) and how it works you can find on its page.

## Projects Goal

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
