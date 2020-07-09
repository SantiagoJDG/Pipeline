#Django
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

#Local model
from authenticator.models import Personal_data


#User creation in admin 
def user_creation(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        password_conf = request.POST['password_conf']

        if password != password_conf:
            return f'Error'
        else:
            return f'Password accepted'

        user = authenticate(username=username, password=password)
        if user:
            user = User.objects.create_user(username=username, password=password)
        else: 
            f'Django Authentication Error'


#In another template, the completion of user data 
def Complete_data(request, user): 

    if request.method == 'POST':

        user.last_name = request.POST['username']
        user.first_name = request.POST['password']
        user.nationality = request.POST['nationality']
        user.city = request.POST['city']
        user.birth_date = request.POST['birth_date']
        user.height = request.POST['height']
        user.weight = request.POST['weight']
        user.save()

        data_info = Personal_data(user=user)
        data_info.save()




        

        
    




        
        
        



        



        





