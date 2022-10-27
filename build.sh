#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
pip install -r requirements.txt
python manage.py migrate
