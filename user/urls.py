from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('profile/', views.profile, name="user-profile"),
   path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="user-login"),
   path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name="user-logout"),
   path('register/', views.register, name="user-register"),
   path('forgetPW/', views.forgetPW, name="user-forgetPW"),
   path('resetPW/', views.resetPW, name="user-resetPW"),
   path('emailsent/', views.emailsent, name="user-emailsent"),
   path('completePW/', views.completePW, name = "user-completePW")
]