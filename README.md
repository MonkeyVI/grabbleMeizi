# grabbleMeizi

New Grabble

virtualenv venv/

source venv/bin/activate

pip install -r requirements.txt

brew install mysql

#init DataBase
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# translation
pybabel compile -f -d translations/

#celery
python manage.py celery run_worker
