from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patients")
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class HeartRate(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="heart_rates")
    bpm = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.bpm} bpm"
