from django.contrib import admin
from django.urls import path
from authenticator import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.user_creation, name='auth'),
]
