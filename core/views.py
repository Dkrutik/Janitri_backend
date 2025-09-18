from rest_framework import generics, permissions,status
from django.contrib.auth import get_user_model
from .models import Patient, HeartRate
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientSerializer

    # GET /api/patients/
    def get(self, request):
        patients = Patient.objects.filter(user=request.user)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST /api/patients/
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientSerializer

    # GET /api/patients/<id>/
    def get(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk, user=request.user)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HeartRateListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HeartRateSerializer

    # GET /api/heart-rates/
    def get(self, request):
        heart_rates = HeartRate.objects.filter(patient__user=request.user)
        serializer = HeartRateSerializer(heart_rates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST /api/heart-rates/
    def post(self, request):
        serializer = HeartRateSerializer(data=request.data)
        if serializer.is_valid():
            patient_id = request.data.get("patient")
            try:
                patient = Patient.objects.get(id=patient_id, user=request.user)
            except Patient.DoesNotExist:
                return Response({"error": "Invalid patient for this user"}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save(patient=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
