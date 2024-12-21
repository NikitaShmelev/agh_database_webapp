from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import CustomUser


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20, unique=True)
    major = models.CharField(max_length=100)
    year_of_study = models.PositiveIntegerField(null=True, blank=True)
