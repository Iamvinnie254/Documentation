# Django is a backend server-side web framework
# It empasizes on reusability of components, also known as DRY (Don't Repeat Yourself), and comes with ready to use features such as login system, database connection and CRUD operations(create, read, update and delete)
# It follows the MVT design pattern (Model View Template)
#        - Model - The data you want to present, usually data from a database
#        - View - A request handler that returns the relevant template and content - based on the request from the user
#        - Template - a text file(like html file) containing the layout of the web page, with logic on how to display the data


###########process

""" 
Install django

- python -m pip install Django

- python --version
- pip --version
- django-admin --version

###Starting a project######

1. django-admin startproject myproject
2. python manage.py runserver    ---to run the project

##Creating an app##
- an app is a web application that has a specific meaning in your project, like a homepage, contact form or a members database

3. python manage.py startapp appname


- in views.py is where we gather information we need to send back a proper response
-django views are python functions that take http requests and return http response, like html documents

####models#####

Allows us to create objects called modelds, which are tables in the database

 """

