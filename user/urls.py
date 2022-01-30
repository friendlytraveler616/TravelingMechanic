from django.urls import path, include
from .views import SearchDetailView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
<<<<<<< HEAD
=======
   path('profile/', views.profile, name="user-profile"),
   path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="user-login"),
   path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name="user-logout"),
   path('register/', views.register, name="user-register"),
   path('user_reviews/', views.user_reviews, name='user-reviews'),
>>>>>>> 880a134c15f924bdacf361592a1bd31ea7aaa66d
   path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/resetPW.html'), name="password_reset"),
   path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/completePW.html'), name = "password_reset_done"),
   path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/resetPWConfirm.html'), name="password_reset_confirm"),
   path('search/', views.search, name="user-search"),
   path('search/<int:pk>/', SearchDetailView.as_view(), name='user-detail'),
   #path('emailsent/', views.emailsent, name="user-emailsent"),
   #path('security/', views.security, name = "user-security")
]
