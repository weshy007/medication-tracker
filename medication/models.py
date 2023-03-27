from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Medication(models.Model):
    # route of administration of the medication
    ROUTES = [
        ('Oral', 'Oral'),  # via mouth
        ('Intravenous', 'Intravenous'),  # into veins(needles)
        ('Topical', 'Topical')  # applied directly to a part
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    route = models.CharField(choices=ROUTES, max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medications")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class MedicationLog(models.Model):
    medication = models.CharField(Medication, max_length=255)
    date_taken = models.DateTimeField(auto_now_add=True)
    dosage_taken = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.medication


class Reminder(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    reminder_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

