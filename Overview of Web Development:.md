Overview of Web Development:
        Browser -- Sends Request --> Google.com --sedns back response --> Browser
        This operation is based on unified protocol named http(HyperText Transfer Protocol) protocol -->> it defines a set rules which are unified so that application across the Internet know how to exchange data with each other and communicate each other.

        https protocol(HyperText Transfer protocol secure)- It is same as http, it also add encryption to our request so thet when a request goes from browser to the server, if there is a praying eye there, somebody that would like to see what kind of data is the  sending to the actual server is locked and when the response comes back is also encrypted and hence anybody who intercepts our request in the middle cannot actually understand what's going on.

        GET request
        POST request
        PUT request
        DELETE request

Django Introduction:
        why python?
        - Django is web development framework that is built using Python.
        - Easy to learn and understand language.
        - Huge Developer Community
        - Written in C - High Performance, ability to link to C.
        - interpreted language compiled on the fly into bytecode.
        - Supports object Oriented design paradiagms
        - easy to maintain, follows don't repeat yourself concept

        What is Django?
        - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
        - Djnago is developed by experienced developers, and it takes care of much of hassel of web development, so that we as web developers can focus on writing our web apps without needing ti reinvent the wheel.
        - Django out of the box provides us with a lot of functionality that we can basically use within our actual application development to quickly implement features into our application, such as for example authentication, form handling, working with SQL database, security concerns and a whole host other application.
        - Django is free and open source.

        Why Django?
                1. Ridiculously Fast -  quick prototyping, and app development
                2. Secure - security is baked into the framework
                3. Scalable - quick and flexibly change scale.
                4. Reusability - application logic divided into smaller apps
                5. Community - Huge developer community. 63.2k Github
        
        Features
                1. MVC(Model - View - Controller) Design pattern
                        model - data for the application
                        view - how the data is dispalyed to the user and information is collected from the user
                        controller - which is this midpoint basically connects our model to our view and basically does the middleman job of controlling the logic in the middle
                2. Built-in Powerful ORM(Object Relational Mapping) : It allow us to basically interact with the SQL database by using Python.
                3. Middleware - CSRF(cross-site resource forgery) Protection, Caching, Authentication...
                4. Flexibility Templating Language- means we can use djago to write HTML documnets in which we can basically place templates tags that can allow us at runtime when the request is served to the user to basically inject dynamic data into our HTML Templates and then render them to the screen.
                5. Server-side Rendering - our application is highly performat,It's going to be search engine optimized, and it's basically going to make our application a lot secure, because most of the actual logic of rendering the application and what needs to happen is done on server side.
                6. Excellent Documentation
                7. Built-Form Handling
        
        Documentation
                1. Official Website : https://www.djangoproject.com/
                2. Documentation : https://docs.djangoproject.com/en/4.0
                3. Download : https://www.djangoproject.com/download/
                4. Source Code : https://github.com/django/django

Getting Started
        Install Python
                1. Download latest Python version from the Python Official website(https://www.python.org/downloads/)
        
        Creating Python Virtual Environment
                1. cmd : python -m pip install virtualenv
                2. Navigate to folder where we need to have virtual environment
                3. cmd : python -m virtualenv venv
                4. cmd : <venv>/Scripts/activate.bat

        Setting up Visual Studio
                1. Extensions a. Django -by Baptiste Darthenay
                              b. Django -by Roberth Solis
                              c. Django Template -by Bibhasdn
                              d. Python -by Microsoft
                              e. Material Icon Theme -by Philipp Kief

        Create Django Project
                1. Activate the Python Virtual Environment
                2. cmd : pip install Django
                3. cmd : django-admin help
                4. cmd : django-admin startproject automax              - Our Django application is composed of many smaller apps, one among is the project_name 
                5. cmd : python manage.py runserver
                
        Django Project structure
                1.app - Django Project that we create is a composition of smaller sub apps that come together to basically form a complete application.
                - Our project have the app with the name as of the projet name.
        
                manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

                mysite/: A directory that is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

                mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.

                mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.

                mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.

                mysite/asgi.py:(Asynchronous server gateway inteface) : It basically allows external applications that act as web servers to basically interact with our Django application and service. An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.

                mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.


Django Basics
        
        Django Apps - cmd : "python manage.py startapp main"
                1. Migrations folder : Object Relational mapper basically creates a SQL Code from our Python Code. which then applies to our database Schema/Database Structure and confirms to the structure that our Django app expects
                                - For every app we have, for every models that app has, the migrations for that are stored within migrations folder.
                2. __init__ : It is the folder used to map the python package that can be imported and used
                3. admin.py : add functionality for our application, which basically pertains to anything that we would want to add to admin panel
                4.apps.py - file which specifically store the information for the particular app that we've created.
                5. models.py - stores all the models that are going to pertaining to this app.Python classes which are basically represent distinct data types, distinct entities or think them as tables in a sql database or basically the schema or the structure that we basically give to our data that can then be stored in a database. In precise models.py allows us to create a python classes and each class is responsible for creating a table in our databsae which can then store information regarding whatever that model represents.
                6. test.py - file in which we are going to place unit test on certain functionality of our app
                7. views.py - file where we define the functionality like of the request

        Working with Django Views
                view.py
                   from django.http import HttpResponse
                   from django.shortcuts import render
                    def landing_view(request):
                        return HTTPResponse("<h1>Welcome to automax </h1>")
                automax/urls.py
                   