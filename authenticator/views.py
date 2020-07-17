#Django
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

#Local model
from authenticator.models import Personal_data

from django.db.utils import IntegrityError


#User creation in admin 
def login_view(request):

    if request.method == 'POST':
        
        username = request.POST['Username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'step_two.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid username and password'})

    return render(request, 'login.html')


#In another template, the completion of user data 
def create_users(request): 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'create_users.html', {'error': 'Password confirmation does not match'})
        
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'login.html', {'error': 'Username is already in user'})
                
        user.email = request.POST['email']
        user.last_name = request.POST['last_name']
        user.first_name = request.POST['first_name']
        nationality = request.POST['nationality']
        city = request.POST['city']
        birth_date = request.POST['birth_date']
        height = request.POST['height']
        weigth = request.POST['weight']
        
        user.save()
        personal_data = Personal_data(user=user, city=city, nationality=nationality, birth_date=birth_date, height=height, weigth=weigth)
        personal_data.save()  

        return render(request, 'step_two.html')

    return render(request, 'create_users.html')

def show_data(request):
    pass 
    
    return(request, 'step_two.html')

def logout_view(request):
    
    logout(request)
    return render(request, 'login.html')


        

        
    




        
        
        



        



        





