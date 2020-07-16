#Django
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Personal_data(models.Model):

    #Using User model from django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #New fields to the personal_data table
    nationality = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=15, blank=False) 
    birth_date = models.DateField(blank=True)
    height = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    weigth = models.IntegerField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
    


