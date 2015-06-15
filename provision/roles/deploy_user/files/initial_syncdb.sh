#!/bin/bash

# Assumes we are chdir'ed to last build dir...

source .virtualenv/bin/activate

python manage.py migrate --noinput

touch $HOME/.initial_syncdb
