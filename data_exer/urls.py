from django.contrib import admin
from django.urls import path
from authenticator import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.login_view, name='auth'),
    path('user_creation/', auth_views.create_users, name='creation')
]
