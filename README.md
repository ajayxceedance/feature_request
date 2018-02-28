# Feature Request POC

A web application that allows the user to create "feature requests".A "feature request" is a request for a new feature that will be added onto an existing piece of software.

# Technologies Used
```
Server Side - Python 3.6.4

Framework - Django 1.11, Django rest framework 3.7.7

Database and ORM - SQLite with Django ORM

Web technologies - HTML5, CSS3, Jquery, KnockoutJS

```


# Getting Started:
```
To get up and running, simply do the following:

First Clone Project on your Local System:

$ git clone https://github.com/ajayxceedance/feature_request.git

# Go to Project Directory
$ cd feature_request

# create enviorment and activate it
$ virtualenv venv
$ source venv/Script/activate
 
# Install the requirements
$ pip install -r requirements.txt

# Perform database mirations
$ python manage.py makemigrations
$ python manage.py migrate

$ Create super user
# python manage.py createsuperuser

$ Running application locally
# python manage.py runserver
```

Note : Bydefault my application will run on 8000 port.



# Admin Site

You can open your browser and type http://localhost:8000/admin to see Django's default Login page
Use following credentials to login
```
username - admin@gmail.com
password - password@111
```

#### You can perform all CRUD operations (like add, update, delete) on Client, Product and Feature data.
