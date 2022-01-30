from django.shortcuts import render, redirect
from .forms import UserRegistForm, userUpdateForm, webUserUpdateForm
from travelingMechanic.models import review
# Create your views here.
def profile(request):
    #Updating requires instance
    if (request.method == 'POST'):
        uForm = userUpdateForm(request.POST, instance=request.user)
        wForm = webUserUpdateForm(request.POST, request.FILES,  instance=request.user.webuser)
        if (uForm.is_valid() and wForm.is_valid()):
            uForm.save()
            wForm.save()
    else:
        uForm = userUpdateForm(instance=request.user)
        wForm = webUserUpdateForm(instance=request.user.webuser)
    context = {"title":"profile", "uForm":uForm, "wForm":wForm}
    return render(request, 'user/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('user-login')
    else:
        form = UserRegistForm()
    context = {"title":"Registration", 'form':form}
    return render(request, 'user/register.html', context)

def user_reviews(request):
    reviewFiltered = review.objects.all().filter(target=request.user.webuser)
    #make the review personalized!
    context={'title':'Reviews', 'reviews':reviewFiltered}
    return render(request, 'user/user_reviews.html', context)
