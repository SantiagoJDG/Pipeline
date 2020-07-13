#Django
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render

#Local model
from authenticator.models import Personal_data


#User creation in admin 
def user_creation(request):

    if request.method == 'POST':
        
        username = request.POST['Username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'login.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid username and password'})

    return render(request, 'login.html')


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




        

        
    




        
        
        



        



        





