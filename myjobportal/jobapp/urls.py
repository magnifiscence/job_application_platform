from django.urls import path
from .views import JobListingListCreate, ApplicationListCreate, UserListCreate

urlpatterns = [
    path('job-listings/', JobListingListCreate.as_view(), name='job-listings-list-create'),
    path('applications/', ApplicationListCreate.as_view(), name='applications-list-create'),
    path('user/', UserListCreate.as_view(), name='user-list-create'),
    # Add more routes as needed
]
