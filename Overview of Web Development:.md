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
                