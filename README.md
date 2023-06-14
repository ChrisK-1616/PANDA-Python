# PANDA-Python
Aire Logic Tech Test Portal: Patient Appointment Backend - write a CRUD backend which stores patient demographic and appointment data

The solution has been built using Python 3.11 and Django 4.2.2

In order to deploy the API both Python and Django need to be installed. Once Python 3.11 is install on the target host machine Django can be installed using pip:-

pip install django

Once Django is installed the distribution from GitHub can be cloned into a known folder on the target host.

From a terminal shell on the target machine (e.g. Windows terminal), change into the root folder of the API distribution (i.e. where the script "manage.py" is
located) and run the following to build the database from the Django model migration facility:-

python manage.py migrate

The result of this should be an SQLite3 database file (named "db.sqlite3") in the API root folder. This contains the necessary tables for the data model and
each of these will be empty.

To test the API the Django HTTP server can be employed (listening on port 12864) by running the command:-

python manage.py runserver 12864

Test the HTTP server is operational by navigating to 127.0.0.1:12864/admin in a web browser, the Django admin login page should be seen. You do not need to
use this but it is an indication that all is well so far.




