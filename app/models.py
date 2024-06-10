from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Customer(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    desc = models.TextField()
    phone =models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+\d{1,3}\d{9,12}$', message="Phone number must be entered in the format: '+999999999'")]
    )

class Applicant(models.Model):
    POSITION_CHOICES = [
        ('senior-software-engineer', 'Senior Software Engineer'),
        ('project-manager', 'Project Manager'),
        ('it-consultant', 'IT Consultant'),
        ('data-analyst', 'Data Analyst'),
        ('network-engineer', 'Network Engineer'),
    ]
    name= models.CharField(max_length=100)
    email = models.EmailField()
    phone =models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+\d{1,3}\d{9,12}$', message="Phone number must be entered in the format: '+999999999'")]
    )
    position = models.CharField(max_length=30, choices=POSITION_CHOICES)
    resume = models.FileField(upload_to='resumes/')
   