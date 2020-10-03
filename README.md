# RestMemberCrawler

This is a djangorestframework and Scrapy project which crawls a specific site to get information, then adds it to a database and has 3 endpoints for specific operations.

- list
- search
- mp 

This instructions assume that you have `Django` and `pip` already istalled.
 - Download the project
 - Add the secret key to `restmembercrawler\settings.py`

 - `pip install djangorestframework`
 - `pip install django-filter`
 - `pip install setuptools`
 - `pip install Scrapy`
 - `pip install jsonschema`

 After this, navigate to the root folder of the project and run:
  - `python manage.py migrate`
  - `python manage.py createsuperuser`
  - `python manage.py runserver`

  To get the data using the Scrapy app from this project, navigate to the 'crawling' directory and run:
  - `scarpy crawl crawling` 
  Wait for the crawling to finish (it might take a few minutes).

  Login with your super user credentials which you have created in the previous step.
  Follow the documentation which is included in each endpoint.
