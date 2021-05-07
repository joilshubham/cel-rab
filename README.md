Follow the below steps to install and the test the application

1. Install and start the rabbitmq server

2. Create an env and install dependencies from requirement.txt

3. If running on windows,
    Since Celery doesn't officially support Windows additional 'gevent' dependency is installed i.e to run Celery worker run 'celery -A app_main worker -l info -P gevent' command
    
    
    'django-celery-results' is used as Celery's results backend which uses the same sqlite3 database as the application and can be viewed in admin panel for testing
    
    'flower' is also used to visually represent the Celery's transactory data at 'http://localhost:5555'. Use 'celery -A app_main flower' command to run flower 
