from __future__ import unicode_literals
from django.db import models

# Create your models here.

ASKER_CHOICES = [
    ('student', 'Student'),
    ('parent', 'Parent'),
    ('school', 'School'),
    ('teacher', 'Teacher'),
    ('others', 'Others'),
    ]


class PostMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    asker = models.CharField(choices=ASKER_CHOICES, max_length=10)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=20000)
    contact_time = models.TimeField(blank=True, auto_now_add=True)


class ContactInfo(models.Model):
    address = models.CharField(max_length=300)
    phoneNumber1 = models.CharField(max_length=13)
    phoneNumber2 = models.CharField(max_length=13)
    email1 = models.EmailField()
    email2 = models.EmailField()

