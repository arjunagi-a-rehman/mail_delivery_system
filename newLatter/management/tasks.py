from celery import shared_task
from .models import User
from django.urls import reverse
from django.core.mail import send_mail
import os


@shared_task
def send_subscription_emails():
    unsubscribed_users = User.objects.filter(isSubscribed=False)

    for user in unsubscribed_users:
        subject = 'Subscribe to our newsletter'
        message = f'Dear {user.name},\n\nPlease subscribe to our newsletter to receive updates and news.\n\nClick here to subscribe: {reverse("subscribe")}\n\nBest regards,\nThe Newsletter Team'
        from_email = os.environ.get('SENDER_EMAIL')
        to_email = [user.email]
        send_mail(subject, message, from_email, to_email)

@shared_task
def send_news_latter_emails():
    unsubscribed_users = User.objects.filter(isSubscribed=True)

    for user in unsubscribed_users:
        subject = 'Exiting news'
        message = f'Dear {user.name},\n\nPlease find The newlatter below in the pdf format'
        from_email = os.environ.get('SENDER_EMAIL')
        to_email = [user.email]
        send_mail(subject, message, from_email, to_email)

