from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.urls import path, include, re_path


urlpatterns = [
	# Registration URl
    path('registration/', views.RegisterView, name='register'),

    #path('login/', auth_views.login, {'template_name': 'auth/login.html'}, name='login'),
    path('', include('django.contrib.auth.urls'), name='login'), 

    # logout url
    path('', include('django.contrib.auth.urls'), name='logout'), 

    # profile URL
    path('profile/', views.ProfileView, name='profile'),

    # Edit Profile URl
    path('profile/edit/', views.EditProfile, name='editprofile'),

    # All User List URl 
    path('users/', views.UserListView, name='userlistview'),


    
]





'''
The URLs provided by auth are:

accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']


'''