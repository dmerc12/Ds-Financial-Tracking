#!/bin/bash

# get database info
echo "Please provide the database information:"
read -p "Database Host: " dbhost
read -p "Database Port: " dbport
read -p "Database Name: " dbname
read -p "Username: " dbuser
read -s -p "Password: " dbpass
echo

# construct the PostgreSQL connection URL
echo "Building database URL... Please wait..."
dburl = "postgresql://$dbuser:$dbpass@$dbhost:$dbport/$dbname"

# get initial admin user info
echo "Please provide the initial admin user info"
read -p "Admin Username: " adminuser
read -p "Admin Email: " adminemail
read -s -p "Admin Password: " adminpass
echo

# install dependencies
echo "Installing dependencies... Please wait..."
pip install django django-crispy-forms crispy-bootstrap5 plotly pandas
python3 manage.py makemigrations
python3 manage.py migrate
cd ./version2/

# set the database connection in Django settings.py
echo "Updating database settings... Please wait..."
sed -i "s/DATABASES = {/DATABASES = {\
\n    'default': {\
\n        'ENGINE': 'django.db.backends.postgresql',\
\n        'NAME': '$dbname',\
\n        'USER': '$dbuser',\
\n        'PASSWORD': '$dbpass',\
\n        'HOST': '$dbhost',\
\n        'PORT': '$dbport',\
\n    }\
\n}/g" main/settings.py

# create initial admin user
echo "Creating admin user... Please Wait..."
python3 manage.py createsuperuser --username $adminuser --email $adminemail --noinput

# run unit tests
echo "Running unit tests... Please Wait..."

# run end to end tests
echo "Running end to end tests... Please Wait..."
