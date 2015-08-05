# grabbleMeizi

New Grabble

virtualenv venv/

source venv/bin/activate

pip install -r requirements.txt

brew install mysql

# translation
pybabel compile -f -d translations/

#celery
python manage.py celery run_worker
