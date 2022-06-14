[![](https://badgen.net/badge/icon/awesome?icon=awesome&label)](https://dvmn.org/)
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
### Environment variables
.env variables are used for security purposes in this project.

To setup them you should create .env file in your settings.py directory
and define all personal database and secret key options of your porject in environment (.env) file.:

```DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME``` for DataBase settings.

```ALLOWED_HOSTS=[127.0.0.1,localhost]``` list of allowed hosts. 

```DEBUG=True``` swap to True for production purposes.

```SECRET_KEY=USE_YOUR_SECRET_KEY``` secret key of project. Setup before running in production.




You can see example in [example.env](https://github.com/triple-s-rank/django-orm-watching-storage/blob/master/project/example.env) file:
```
SECRET_KEY=USE_YOUR_SECRET_KEY
DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
DEBUG=True
ALLOWED_HOSTS=[127.0.0.1,localhost]
```
More information about [environs lib](https://pypi.org/project/environs/) and how it works.

### Running
To run enter command in manage.py directory
```$ python manage.py runserver 0.0.0.0:8000```

Than put url ```http://127.0.0.1:8000/``` (by default) in your browser.

## How it works

datacenter\models.py contents orm models:

- Passcard models- passcard information.
- Visit models - storage visits information.
- Method is_visit_long of Visit object and returns boolean. Shows if visit is suspicious (by default suspicious will be 60 and more minutes)
- Method get_duration of Visit object returns timedelta object of visit duration.
- Method format_duration of Visit object converts timedelta in readable HH:MM:SS

datacenter\active_passcards_view.py shows list of active passcards.

datacenter\storage_information_view.py shows list of employees who are in storage now.

datacenter\passcard_info_view.py shows visit history of employee.

datacenter\templates\ HTML templates.

## Projects Goal

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
