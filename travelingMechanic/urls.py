from django.urls import path
from .views import CommissionCreateView, CommissionDetailView, CommissionDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('commissions/', CommissionCreateView.as_view(), name='commissions'),
    path('commission/<int:pk>/', CommissionDetailView.as_view(), name='commission-detail'),
    path('commission/<int:pk>/delete', CommissionDeleteView.as_view(), name='commission-delete'),
    path('review/', views.review, name='review-page'),
]