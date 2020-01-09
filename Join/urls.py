from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='Join/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Join/logout.html'), name='logout'),
    path('userlist/', Userlist, name='Userlist'),
    path('', login_success, name='login_success'),
]