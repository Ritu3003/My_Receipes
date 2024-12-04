from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Radmin(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='up_media/', blank=True, null=True)  # Specify the upload folder
    description = models.CharField(max_length=255, blank=True, null=True)  # Fixed the typo here
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    contact = models.IntegerField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name


