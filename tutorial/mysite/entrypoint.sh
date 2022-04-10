#!/bin/bash/

# collect static files
python manage.py collectstatic --noinput
# database migrations
python manage.py makemigrations     # create migrations 
python manage.py migrate            # apply migrations   
# start the server
python manage.py runserver 0.0.0.0:8000
