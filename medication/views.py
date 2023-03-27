from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework.response import Response

from .tasks import send_reminder_email
from .models import Medication, MedicationLog, Reminder
from .serializers import MedicationSerializer, MedicationLogSerializer, ReminderSerializer


# Create your views here.
class MedicationListView(generics.ListAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated, ]


class MedicationCreateView(generics.CreateAPIView):
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated]


class MedicationUpdateView(generics.UpdateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated, ]


class MedicationDeleteView(generics.DestroyAPIView):
    queryset = Medication.objects.all()
    permission_classes = [IsAuthenticated, ]


class MedicationLogView(generics.ListAPIView):
    queryset = MedicationLog.objects.all()
    serializer_class = MedicationLogSerializer
    permission_classes = [IsAuthenticated, ]


class MedicationLogCreateView(generics.CreateAPIView):
    serializer_class = MedicationLogSerializer
    permission_classes = [IsAuthenticated]


class ReminderCreateView(APIView):
    serializer_class = ReminderSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            medication = serializer.validated_data["medication"]
            reminder_time = serializer.validated_data["reminder_time"]
            enabled = serializer.validated_data['enabled']

            # Save the reminder to db
            reminder = Reminder.objects.create(
                medication=medication,
                reminder_time=reminder_time,
                enabled=enabled
            )

            # Send reminder email
            subject = 'Medication Reminder'
            message = f"Remember to take {medication.name} at {reminder_time} today!"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [request.user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            # Schedule reminder push notification using Celery
            now = timezone.now()
            notification_time = datetime.combine(now.date(), reminder_time)

            if notification_time < now:
                notification_time = notification_time + timedelta(days=1)
            send_reminder_email.apply_async(args=[medication.name, notification_time.isoformat()])

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_notification(medication_name, notification_time):
    # TODO: push notification
    # To send push notifications, you can use a push notification service like
    # Firebase Cloud Messaging(FCM).
    pass


