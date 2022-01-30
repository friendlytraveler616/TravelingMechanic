from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('profile', views.profile, name="user-profile"),
<<<<<<< HEAD
   path('login', views.login, name="user-login"),
=======
   path('login', auth_views.LoginView.as_view(template_name='user/login.html'), name="user-login"),
   path('logout', auth_views.LogoutView.as_view(template_name='user/logout.html'), name="user-logout"),
>>>>>>> 5ff21765d46e865217690cef37c2c7cf7e4ceec1
   path('register', views.register, name="user-register"),
   path('forgetPW', views.forgetPW, name="user-forgetPW")
]