from django.contrib import admin
from django.urls import path
from authenticator import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/login/', auth_views.login_view, name='auth'),
    path('auth/login/user_creation/', auth_views.create_users, name='user_creation'),
    path('auth/usersland/', auth_views.CD_form_view, name='data_completion'),
    path('logout/', auth_views.logout_view, name='logout'),

]
