python3 ./src/manage.py makemigrations
python3 ./src/manage.py migrate
python3 ./src/manage.py runserver 0.0.0.0:8000
python3 ./src/manage.py loaddata db.json