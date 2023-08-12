# Logistics App

# Transift Logistics Application with user registration, login, search and CRUD with Django.

# Class Based Views links:

- [Django CBV Documentation](https://docs.djangoproject.com/en/4.0/ref/class-based-views/)
- [Django Views Source code](https://github.com/django/django/tree/master/django/views/generic)
- [Detailed descriptions for each of Django's class-based views.](http://ccbv.co.uk/)


![image](https://github.com/venkatapechetty-01/TranswiftInc/assets/137584556/902d3bb1-a4a6-4c65-8722-0e3e055d6c43)

# Main Features:

* User Interface (UI) Module
* Authentication and User Roles Module
* Database Management Module
* Driver Management Module
* Vehicle Scheduling Module
* Delivery Tracking Module

# Usage:

To use this template to start your own project:

### Existing virtualenv

If your project is already in an existing python virtualenv first install django by running

    $ pip install django

And then run the `django-admin.py` command to start the new project.
      
### No virtualenv

This assumes that `python` is linked to valid installation of python and that `pip` is installed and is valid for installing python packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python then run:

    $ pip install django

    $ django-admin.py startproject <project_name>
          
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# {{ project_name|title }}

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
        
Then simply apply the migrations:

    $ python manage.py migrate
    
You can now run the development server:

    $ python manage.py runserver
