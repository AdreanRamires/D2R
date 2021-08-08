D2R 
---

---
## What is D2R?
    D2R is a Diablo II Resurection support community website
    which is aming to provide players with latest game news,
    trading ground as well as sharing strategies and organising
    tournaments.

___
### Current state of D2R
* Home Page
    * section to the latest news and gallery
    * section apply to become part of the team 

* News 
    * website and game related news to be shared by the admin team
  
* Gallery 
  * image upload feature available for registered users
  * edit and delete options on the uploaded images

* Login & Register functionality
  * profile page available for registered users

___
### Future Long-term Goals features to be implemented

* Account recovery
* Forum and sub forums
* Trade currency - forum gold

___

## Installation

    To install the app, you must have a working Python 3.9 installation and PostgreSQL.
    
### Required Python libraries 

  * Django
  * Pillow
  * Psycopg2
  * Asgiref
  * Sqlparse
  * Pytz

To automatically install requirements run the following command:

    pip install -r requirements.txt

### Postgres
Initially the app will expect a database user _**postgres**_ with password _**112QwER**_ and a database called _**postgres**_. 
  

### First time setup

Before running the app for the first time, you should set up the database through Django. You can do this by running the
following commands:
    
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py createsuperuser

Afterwards, you can run the app by running the following command:
    
    - python manage.py runserver

## Author
  Written and maintained by A Ramires
  