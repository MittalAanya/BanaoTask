from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # Add additional fields
    USER_TYPE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField('username', max_length=10, unique=True, db_index=True)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.username
    

