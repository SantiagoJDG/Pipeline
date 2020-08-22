from django.shortcuts import render

# Create your views here.

def tests_views(request):
    
    return render(request, 'tests.html')