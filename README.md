# Newsletter Service

The Newsletter Service is a Django project designed to manage newsletter subscriptions, send subscription emails using Celery, and log subscription activities in MongoDB. Users can also schedule newsletters for future delivery.

## Features

- User management: Allows users to subscribe to the newsletter service.
- Subscription emails: Sends subscription confirmation emails using Celery and AWS SQS as the message broker.
- Logging: Logs subscription activities in MongoDB for analytics and tracking purposes.
- Newsletter scheduling: Users can schedule newsletters for future delivery.

## Technologies Used

- Django: Web framework used for backend development.
- Celery: Distributed task queue used for asynchronous processing of subscription emails as well as for scheduling.
- AWS SQS: Message broker used for communication between Django and Celery and act as a queue for message processing between beat and worker.
- MySQL: Relational database used for user and job management.
- MongoDB: NoSQL database used for logging subscription activities.

## Setup Instructions

1. Clone the repository to your local machine:

```
git clone <repository-url>
```
2. Go to news Latter
```
cd newLatter
```
2. Install the required Python packages using pip:

```
pip install -r requirements.txt
```

3. Set up the MySQL and MongoDB databases and update the Django settings accordingly.

4. Configure Celery to use AWS SQS as the message broker. Update the `BROKER_URL` in the Celery configuration.

5. Run database migrations:

```
python manage.py migrate
```
```
python manage.py migrate django_celery_beat
```
6. Start the Celery worker:

```
celery -A newLatter worker -l info
```

7. Start the Django development server:

```
python manage.py runserver
```

## Usage

- Access the Django admin interface to manage users and subscriptions.
- Use the provided APIs to interact with the service programmatically.
- Monitor Celery logs for task execution and SQS for message queueing.
- Analyze subscription activity logs stored in MongoDB.
- Schedule newsletters for future delivery through the user interface.

# For the react pay subscription page and it's deployment refer to the redme from pay-and-subscribe-page


