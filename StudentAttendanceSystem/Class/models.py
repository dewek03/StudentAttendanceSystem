from django.db import models
from User.models import Student

class ClassSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    time = models.TimeField()
    max_participants = models.IntegerField()

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(ClassSession, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
