#Django
from django.db import models
from django.contrib.auth.models import User

class Personal_data(models.Model):

    #Using User model from django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #New fields to the personal_data table
    country = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=15, blank=False) 
    birth_date = models.DateField('%Y-%m-%d', blank=False)
    
    class gender(models.Model):
        
        FEMALE = 'F'
        MALE = 'M'
        NOT_IDENTIFIED = 'NI'
        
        GENDER_CHOICES = [
            ( MALE, 'MALE'),
            ( FEMALE, 'FEMALE'),
            ( NOT_IDENTIFIED, 'NOT IDENTIFIED')
        ]
        gender = models.CharField(
            
            max_length=2,
            choices= GENDER_CHOICES,
            default= None
        )         

        def is_upperclass(self):
            return self.gender in {self.MALE, self.FEMALE}

    height = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    weigth = models.IntegerField(blank=False)
    
    class blood_type(models.Model):

        O_negative = '0-'
        O_positive = 'O+'
        A_negative = 'A-'
        A_positive = 'A+'
        B_negative = 'B-'
        B_positive = 'B+'
        AB_negative = 'AB-'
        AB_positive = 'AB'
        
        BLOOD_TYPE_CHOICES = [
            (O_negative, 'O negative'),
            (O_positive, 'O Positive'),
            (A_negative, 'A negative'),
            (A_positive, 'A positive'),
            (B_negative, 'B negative'),
            (A_positive, 'B positive'),
            (AB_negative, 'AB negative'),
            (AB_positive, 'AB positive')
            ]

        blood_type = models.CharField (
            max_length=12,
            choices= BLOOD_TYPE_CHOICES,
            default= None
        )    

        def is_upperclass(self):
            return self.blood_type in {self.A_positive, self.O_negative}


    Created = models.DateTimeField(auto_now_add=True),
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
    


