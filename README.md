# PANDA-Python
Aire Logic Tech Test Portal: Patient Appointment Backend - write a CRUD backend which stores patient demographic and appointment data

Note - when reading the following please also refer to the code comments made within the relevant Python scripts for more insight into the operation of the
scripts. The relevant script files are:-

  appointments/models.py
  appointments/views.py
  appointments/urls.py
  appointments/helpers.py
  appointments/tests.py
  
These can all be found in the root folder once the GitHub repository for the API has been cloned.


Installation Of Testing Environment
===================================

The solution has been built using Python 3.11 and Django 4.2.2

In order to deploy the API both Python and Django need to be installed. Once Python 3.11 is install on the target host machine Django can be installed using pip:-

  > pip install django

Once Django is installed the distribution from GitHub can be cloned into a known folder on the target host.

From a terminal shell on the target machine (e.g. Windows terminal), change into the root folder of the API distribution (i.e. where the script "manage.py" is
located) and run the following to build the database from the Django model migration facility:-

  > python manage.py migrate

The result of this should be an SQLite3 database file (named "db.sqlite3") in the API root folder. This contains the necessary tables for the data model and
each of these will be empty.

To test the API the Django HTTP server can be employed (listening on port 12864) by running the command:-

  > python manage.py runserver 12864

Test the HTTP server is operational by navigating to 127.0.0.1:12864/admin in a web browser (suggest Chrome), the Django admin login page should be seen. You do
not need to use the admin functions but it is an indication that all is well so far. Now API calls can be made to the system.


Using the API Calls - General Points
====================================

There are API calls to perform create, retrieve, update and delete functions on the Patient and Appointment tables within the database. All interaction with these
API calls are JSON based. All API calls use the "GET" method. The response from an API will differ depending upon the function but all responses have the following
JSON structure:-

{
  "success": true or false,
  "message": "String indicating feedback from the API call",
  "data": array of any relevant data associated with the API call
}

The "success" element can be used to determine if the API completed successfully whilst the "message" string contains feedback that can be relayed to the frontend
UI. The "data" element will contain the returned details when a retrieve API call is made, otherwise this remains empty for all other API calls.


Patient API Calls
=================

(Note here the instructions will assuming use of the localhost Django HTTP server listening on port 12864)

Create Patient:-
--------------
Make an HTTP client call of the URL form (with example patient data):-
  
  127.0.0.1:12864/create-patient/{"nhs_number": "1373645350", "name": "Dr Glenn Clark", "date_of_birth": "1996-02-01", "postcode": "N6 2FA"}/
  
The supplied patient data will have the NHS Number checksum checked before it is added to the database, if this fails then the create call fails and a suitable
JSON string response is returned. Also, the postcode is coerced to the form:-
  
  Outward Code + " " + Inward Code
  
so all postcodes are stored in this form, for example a supplied postcode "AB123CD" will be coerced into "AB12 3CD", a postcode " E F 3 4 G H " will be coerced
into "EF3 4GH".

On success the database will now contain a new instance of this patient.

Retrieve Patient:-
----------------
Make an HTTP client call of the URL form (with example patient data):-
  
  127.0.0.1:12864/retrieve-patient/1373645350/
  
Note the "1373645350" element of the URL is the NHS Number of the patient to be retrieved and is all that is needed. If there is a patient in the system with
this NHS Number then the details of the patient will be returned in the HTTP response and held in the "data" element of the JSON string. If there is no
patient with the supplied NHS Number then the retrieve call fails and a suitable message is returned in the "message" element of the JSON string.

Update Patient:-
--------------
Similar to the create API call, make an HTTP client call of the URL form (with example patient data):-
  
  127.0.0.1:12864/update-patient/{"nhs_number": "1373645350", "name": "Dr Glenn Clark-Smith", "date_of_birth": "1996-02-01", "postcode": "N6 2FA"}/
  
Again checks are made to ensure an existing patient instance to update and coercing of the postcode. If the update fails then a suitable message is provided
in the HTTP response JSON string.

Delete Patient:-
--------------
Similar to the retrieve API call, make an HTTP client call of the URL form (with example patient data):-
  
  127.0.0.1:12864/delete-patient/1373645350/
  
Where the "1373645350" element of the URL is the NHS Number of the patient to be deleted. If the supplied patient is not recorded in the system then a
suitable message is returned in the HTTP response JSON string and obviously no deletion occurs. Note that since the patient is referred to in appointment
instances, deleting a patient will also cascade to deleting appointments since the patient is no longer valid.


Appointment API Calls
=====================  

(Note here the instructions will assuming use of the localhost Django HTTP server listening on port 12864)

In the case of the appointment models in the system they are keyed by both the patient NHS Number and the datetime of the appointment. This can uniquely
identify an appointment since there is only one patient referred to on the appointment and a patient at any given time can only be at one appointment. To
implement this the key provided for retrieval and deletion of appointment instances is in the JSON string form:-

{
  "patient": "<nhs number>",
  "time": "< datetime string>"
}

So, for example to key an appointment for patient "1373645350" at time "2018-01-21T16:30:00+00:00" the JSON key string would be:-
  
{
  "patient": "1373645350",
  "time": "2018-01-21T16:30:00+00:00"
}
  
and this JSON string is provided in the API call URL where appropriate 

Create Appointment:-
------------------
Make an HTTP client call of the URL form (with example patient data):-
  
  127.0.0.1:12864/create-apppointment//
  
This call will fail to create a new appointment if there existing no patient with the provided NHS Number (this is in the "patient" element of the
JSON string). A suitable message is returned if the create call fails in this manner.
  
Another aspect of the appointment creation is the "clinician" and "department" properties. These are created or retrieved in/from their own data
tables held in the system. Whilst this is not fully realised it does begin to address the need for more detail stored in the system for clinicians and the
departments they operate within.

On success the database will now contain a new instance of this appointment.

Retrieve Appointment:-
--------------------
Make an HTTP client call of the URL form (with example patient data):-
  
  127.0.0.1:12864/retrieve-patient/1373645350/
  
Note the "1373645350" element of the URL is the NHS Number of the patient to be retrieved and is all that is needed. If there is a patient in the system with
this NHS Number then the details of the patient will be returned in the HTTP response and held in the "data" element of the JSON string. If there is no
patient with the supplied NHS Number then the retrieve call fails and a suitable message is returned in the "message" element of the JSON string.

Update Appointment:-
------------------
Similar to the create API call, make an HTTP client call of the URL form (with example patient data):-
  
  127.0.0.1:12864/update-patient/{"nhs_number": "1373645350", "name": "Dr Glenn Clark-Smith", "date_of_birth": "1996-02-01", "postcode": "N6 2FA"}/
  
Again checks are made to ensure an existing patient instance to update and coercing of the postcode. If the update fails then a suitable message is provided
in the HTTP response JSON string.

Delete Appointment:-
------------------
Similar to the retrieve API call, make an HTTP client call of the URL form (with example patient data):-
  
  127.0.0.1:12864/delete-patient/1373645350/
  
Where the "1373645350" element of the URL is the NHS Number of the patient to be deleted. If the supplied patient is not recorded in the system then a
suitable message is returned in the HTTP response JSON string and obviously no deletion occurs. Note that since the patient is referred to in appointment
instances, deleting a patient will also cascade to deleting appointments since the patient is no longer valid.
 
