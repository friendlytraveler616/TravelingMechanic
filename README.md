# TravelingMechanic

![Screenshot 2022-03-22 105423](https://user-images.githubusercontent.com/53315150/159510968-2dd746bf-c224-4279-99c3-862086c4d132.png)

## Setup Instructions

### Install Required Python Modules

Create external python virtual environment then run this command
```bash
pip install -r requirements.txt
```
### Start Web Server

To start the web server you need to run the following sequence of commands.

First cd into DatabaseProject.

Only run this when updating database
```bash
python manage.py makemigrations
python manage.py migrate
```

Next run the django web server.
```bash
python manage.py runserver
```
