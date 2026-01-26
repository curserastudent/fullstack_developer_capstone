#!/bin/sh

echo "Making migrations and migrating the database."
python manage.py makemigrations djangoapp --noinput
python manage.py migrate --noinput

echo "Populating database..."
python manage.py shell -c "from djangoapp.populate import initiate; initiate()"

python manage.py collectstatic --noinput

exec "$@"