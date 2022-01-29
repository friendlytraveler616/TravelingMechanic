from django.urls import path, include
from . import views

urlpatterns = [
   path('profile', views.profile, name="user-profile"),
   path('login', views.login, name="user-login"),
   path('signin', views.signin, name="user-signin"),
   path('register', views.register, name="user-signin"),
   path('forgetPW', views.forgetPW, name="user-forgetPW")
]