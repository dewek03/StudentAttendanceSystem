from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=[('student', 'Student'), ('teacher', 'Teacher')])


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    year_level = models.IntegerField()
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=100)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
