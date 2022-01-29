from django.shortcuts import render
from .models import Commission
# Create your views here.

def home(request):
    context = {
        'commissions': Commission.objects.all(),
        'title': 'Home'
    }

    return render(request, 'travelingMechanic/home.html', context)

