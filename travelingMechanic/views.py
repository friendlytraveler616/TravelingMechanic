from django.shortcuts import render
from django.views.generic import CreateView
from .models import Commission, webUser
from django import forms
import json

# Create your views here.
def home(request):
    data = Commission.objects.filter(lat__isnull=False)
    return render(request, 'travelingMechanic/home.html', {'data': data,'title': 'Home'})

class CommissionCreateView(CreateView):
    model = Commission
    template_name = 'travelingMechanic/commissions.html'
    fields = ['title', 'description', 'askPrice', 'lat', 'long', 'images']

    def form_valid(self, form):
        form.instance.author = webUser.objects.all().filter(user=self.request.user).first()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['lat'].widget = forms.HiddenInput()
        form.fields['long'].widget = forms.HiddenInput()
        form.fields['images'] = forms.ImageField()
        form.fields['images'].required = False
        return form



