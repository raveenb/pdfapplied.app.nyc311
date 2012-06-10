pdfapplied.app.nyc311
=====================

Repo for the pdf applied hackathon project nyc311 #pdfapplied

Team Members
1. Jackson Lin
2. Raveen Beemsingh
3. Stephen Autar

Future contributors please add their names, we will be happy to see if this gets worked beyong this hackathon

Pre-Requisites
- python - you should know this before you start :)
- python virtualenv - http://www.virtualenv.org/en/latest/index.html
- python pip - http://www.pip-installer.org/en/latest/index.html
- linux like development evironment - macosx/linux/cygwin

Steps to Start
1. virtualenv venv --distribute
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py syncdb
5. python manage.py migrate webapp

Steps to run debug server
1. python manage.py runserver_plus - this will start a debug server @ http://localhost:8000 with some cool debugging features

2. homepage is at @ http://localhost:8000/home
