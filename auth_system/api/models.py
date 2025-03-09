from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('SAVED', 'Saved'),
        ('SENT', 'Sent'),
        ('INTERVIEW', 'Interviews'),
        ('FINISHED', 'Finished'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ctc = models.DecimalField(max_digits=10, decimal_places=2)
    resume = models.FileField(upload_to='resumes/')
    description = models.TextField()
    skills = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)