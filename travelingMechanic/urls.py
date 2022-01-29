from django.urls import path
from .views import CommissionListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('commissions/', CommissionListView.as_view(), name='commissions'),
]