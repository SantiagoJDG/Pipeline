#Django
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render

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
            return render(request, 'login.html', {'error': 'Existing User'})
        elif AnonymousUser:
            return render(request, 'create_users.html')
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
        user.nationality = request.POST['nationality']
        user.city = request.POST['city']
        user.birth_date = request.POST['birth_date']
        user.height = request.POST['height']
        user.weight = request.POST['weight']
        
        personal_data = Personal_data(user=user)
        personal_data.save()
        user.save()
        

        
    
    return(request, 'create_users.html')




        

        
    




        
        
        



        



        





