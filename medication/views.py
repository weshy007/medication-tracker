from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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


class ReminderCreateView(generics.CreateAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]
