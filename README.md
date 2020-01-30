# QuotesApi
This is a simple API build using django-rest-framework,<br />
to share stock values downloaded from:https://www.bankier.pl/gielda/notowania/akcje
# How to run it
 - Clone this repo
 - Create Virtualenv in directory where you have cloned this repo
 - Inside this virtualenv install libraries from ```requirements.txt```
 - get inside stock directory and type ```python3 manage.py get_data``` to get data first
 - next simply run app by ```python3 manage.py runserver```
 ## About Views
 Simply there is only one view, it gives us all required data and it's readonly. <br />
 You can also search and order in this view
 ## About Loader
 This module downloads data from given page and saves those to the database if there are no such data, <br />
 if data exists in the database it simply updates current data.
## Additional info
- all needed libraries can be found in requirements.txt
- Available links are ```/admin```, ```/data```
