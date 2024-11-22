### A Simple Subscription Project Using Celery And RabbitMQ
This project include 3 directory:
1. **celery_subscription** directory: This directory is a django project that is uses celery for creating microservices
2. **rabbitmq_subscription** directory: This directory is the same project as **celery_subscription**, but instead of using celery this project uses **pika** package to implement microservices
3. **subscription_apis** directory: This is the api which communicate with MongoDB database.
Also I wrote a simple **End_to_End** test on **end_to_end_testing.py** file with **Selenium**.