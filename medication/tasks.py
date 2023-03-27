from celery import shared_task
from django.core.mail import send_mail

from .models import Reminder


@shared_task
def send_reminder_email(reminder_id):
    reminder = Reminder.objects.get(id=reminder_id)
    subject = 'Reminder: Take your medication!'
    message = f"Don't forget to take your {reminder.medication.name} medication at {reminder.reminder_time} today."
    recipient_list = [reminder.medication.created_by.email]
    send_mail(subject, message, from_email=None, recipient_list=recipient_list)
