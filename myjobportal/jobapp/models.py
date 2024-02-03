from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class JobListing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE)
    # Add more fields as needed

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)

# Lets create a signal to automatically create profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Application(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resume/')
    date_applied = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending') #can be 'pending', 'reviewed', 'accepted', etc
    # Add more fields as needed
