pdfapplied.app.nyc311
=====================

Repo for the pdf applied hackathon project nyc311 #pdfapplied

Team Members
- Jackson Lin
- Raveen Beemsingh
- Stephen Autar

Future contributors please add their names, we will be happy to see if this gets worked beyond this hackathon

Pre-Requisites
- python - you should know this before you start :)
- python virtualenv - http://www.virtualenv.org/en/latest/index.html
- python pip - http://www.pip-installer.org/en/latest/index.html
- development evironment - any, we used macosx/sublimetext2/ipython

Steps to Start
- virtualenv venv --distribute
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py syncdb
- python manage.py migrate webapp

Steps to run debug server
- python manage.py runserver_plus - this will start a debug server @ http://localhost:8000 with some cool debugging features
- homepage is at @ http://localhost:8000/home
