from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name = 'user_auths/loginPage.html'), name='user_login'),
    path('user_logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    #path('user_logout/', auth_views.LogoutView.as_view(template_name = 'user_auths/logoutPage.html'), name='user_logout'),
    path('user_registration', views.user_registration, name='user_registration'),
]