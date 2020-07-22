from django import forms

class Complete_data(forms.Form):

    FEMALE = 'F'
    MALE = 'M'
    NOT_IDENTIFIED = 'NI'

    GENDER_CHOICES = [
        ( MALE, 'M'),
        ( FEMALE, 'F'),
        ( NOT_IDENTIFIED, 'NI')
    ]
        
    nationality = forms.CharField(max_length=20, required=True)
    city = forms.CharField(max_length=15, required=True) 
    birth_date = forms.DateField(required=True)
    gender = forms.ChoiceField(

            choices = GENDER_CHOICES,
            required=True
        )
    height = forms.DecimalField(max_digits=3,required=True)
    weight = forms.IntegerField(max_value=500)

    