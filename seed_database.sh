#!/bin/bash

rm db.sqlite3
rm -rf ./pawsapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations pawsapi
python3 manage.py migrate pawsapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata visitTypes
python3 manage.py loaddata petTypes
python3 manage.py loaddata visitFrequencies
python3 manage.py loaddata actions
python3 manage.py loaddata visits
python3 manage.py loaddata visitActions
python3 manage.py loaddata visitReviews