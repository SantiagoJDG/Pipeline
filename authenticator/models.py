#Django
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Personal_data(models.Model):

    FEMALE = 'F'
    MALE = 'M'
    NOT_IDENTIFIED = 'NI'

    GENDER_CHOICES = [
        ( MALE, 'M'),
        ( FEMALE, 'F'),
        ( NOT_IDENTIFIED, 'NI')
    ]
    
    #Using User model from django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #New fields to the personal_data table
    nationality = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=15, blank=False) 
    birth_date = models.DateField(blank=True, null=True)
    height = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    weigth = models.IntegerField(blank=True, null=True)
    gender = models.CharField(

            choices = GENDER_CHOICES,
            max_length=3,
            blank=True
        )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
    
    

    
    


