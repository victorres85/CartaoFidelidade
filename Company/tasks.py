from __future__ import absolute_import

from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from celery import shared_task

@shared_task
def registration_completed(user_id, confirmation):
    user = User.objects.get(pk=user_id)
    subject = f'Welcome {user.username}, to CartaoFidelidade'
    message = f'''Welcome to CartaoFidelidade.
To confirm your email please use the code below
{confirmation}''' 
    email = EmailMessage(subject, message, 'admin@myshop.com', [user.email])
    email.send()