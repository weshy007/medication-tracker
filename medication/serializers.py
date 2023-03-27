from rest_framework import serializers
from .models import Medication, MedicationLog, Reminder


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ("id", "name", "dosage", "start_date")


class MedicationLogSerializer(serializers.ModelSerializer):
    medication = serializers.CharField(source='medication.name')

    class Meta:
        model = MedicationLog
        fields = ("id", "medication", "date_taken", "dosage_taken", "created_at")


class ReminderSerializer(serializers.ModelSerializer):
    medication = MedicationSerializer()

    class Meta:
        model = Reminder
        fields = ("id", "medication", "reminder_time", "enabled", "created_at", "updated_at")
