from django.shortcuts import render, redirect
from .forms import UserRegistForm
# Create your views here.
def profile(request):
    context = {"title":"profile"}
    return render(request, 'user/profile.html', context)

<<<<<<< HEAD
def login(request):
    context = {"title":"login"}
    return render(request, 'user/login.html', context)

=======
>>>>>>> 5ff21765d46e865217690cef37c2c7cf7e4ceec1
def register(request):
    if request.method == 'POST':
        form = UserRegistForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('user-login')
    else:
        form = UserRegistForm()
    context = {"title":"Registration", 'form':UserRegistForm}
    return render(request, 'user/register.html', context)

def forgetPW(request):
    context = {"title":"Forgot Password?"}
    return render(request, 'user/forgetPW.html', context)