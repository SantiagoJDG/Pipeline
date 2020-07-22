#Django
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

#Local model
from authenticator.models import Personal_data

from django.db.utils import IntegrityError

from authenticator.forms import Complete_data


#User creation in admin 
def login_view(request):

    if request.method == 'POST':
        
        username = request.POST['Username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'completion.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid username and password'})

    return render(request, 'login.html')


def CD_form_view(request):

    complete_data = request.user.personal_data
    if request.method == 'POST':
        form = Complete_data(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            complete_data.gender = data['gender']
            complete_data.nationality = data['nationality']
            complete_data.city = data['city']
            complete_data.birth_date = data['birth_date']
            complete_data.height = data['height']
            complete_data.weight = data['weight']
            complete_data.save()
                
            return redirect('data_completion')
    else: 
        form = Complete_data()
    
    return render(
        request=request,
        template_name='completion.html',
        context={
            'complete_data': complete_data,
            'user': request.user,
            'form': form
        }
    )

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
            return render(request, 'create_users.html', {'error': 'Username is already in use'})       
               
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        
        personal_data = Personal_data(user=user)
        personal_data.save()
        
        login(request, user)
        return render(request, 'completion.html')

    return render(request, 'create_users.html')

def show_data(request):
    pass 
    
    return(request, 'completion.html')

def logout_view(request):
    
    logout(request)
    return render(request, 'login.html')


        

        
    




        
        
        



        



        





