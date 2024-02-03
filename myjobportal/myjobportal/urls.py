"""
URL configuration for myjobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import JobListingListCreate, ApplicationListCreate, UserListCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job-listings/', JobListingListCreate.as_view(), name='job-listings-list-create'),
    path('applications/', ApplicationListCreate.as_view(), name='applications-list-create'),
    path('user/', UserListCreate.as_view(), name='user-list-create'),
    # Add more routes as needed
]
