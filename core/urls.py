from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, PatientListCreateView, PatientDetailView, HeartRateListCreate

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("patients/", PatientListCreateView.as_view(), name="patients"),
    path("patients/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),
    path("heart-rates/", HeartRateListCreate.as_view(), name="heart-rates"),
]
