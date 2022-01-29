from django.shortcuts import render

# Create your views here.
def profile(request):
    context = {"title":"profile"}
    return render(request, 'user/profile.html', context)

def login(request):
    context = {"title":"login"}
    return render(request, 'user/login.html', context)

def register(request):
    context = {"title":"Registration"}
    return render(request, 'user/register.html', context)

def forgetPW(request):
    context = {"title":"Forgot Password?"}
    return render(request, 'user/forgetPW.html', context)