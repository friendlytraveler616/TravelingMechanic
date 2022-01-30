from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Commission, webUser, review
from .forms import createReview
from django import forms
from django.contrib import messages

# Create your views here.
def home(request):

    context = {
        'commissions': Commission.objects.all(),
        'title': 'Home'
    }
    return render(request, 'travelingMechanic/home.html', context)

class CommissionCreateView(CreateView):
    model = Commission
    template_name = 'travelingMechanic/commissions.html'
    fields = ['title', 'description', 'askPrice', 'lat', 'long']

    def form_valid(self, form):
        form.instance.author = webUser.objects.all().filter(user=self.request.user).first()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['lat'].widget = forms.HiddenInput()
        form.fields['long'].widget = forms.HiddenInput()
        return form

def review(request):
    if request.method == 'POST':
        c_form = createReview(request.POST, request.FILES, initial={'author':request.user.webuser})
        if (c_form.is_valid()):
            print(c_form.cleaned_data)
            c_form.save()
            messages.success(request, 'Your review is posted!')
            return redirect('home')
    else:
        c_form = createReview(initial={'author':request.user.webuser})
    context = {'title':'Submit review', 'c_form':c_form}
    return render(request,'travelingMechanic/submitReview.html',context)

