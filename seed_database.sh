#!/bin/bash

rm db.sqlite3
rm -rf ./pawsapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations pawsapi
python3 manage.py migrate pawsapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

