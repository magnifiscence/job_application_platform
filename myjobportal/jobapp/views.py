from django.shortcuts import render

# Create your views here to handle API endpoints.
from rest_framework import generics
from .models import JobListing, Application, User
from .serializers import JobListingSerializer, ApplicationSerializer, UserSerializer

class JobListingListCreate(generics.ListCreateAPIView):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer

class ApplicationListCreate(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
