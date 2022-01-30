from django.urls import path
from .views import CommissionCreateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('commissions/', CommissionCreateView.as_view(), name='commissions'),
    path('review/', views.review, name='review-page')
]