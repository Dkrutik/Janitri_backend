from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Patient, HeartRate

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "name", "age", "gender", "created_at"] 
        read_only_fields = ["id", "created_at"]

class HeartRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartRate
        fields = ["id", "patient", "bpm", "recorded_at"]
        read_only_fields = ["id", "recorded_at"]
