from django.shortcuts import render
from django.views.generic import CreateView
from .models import Commission
# Create your views here.

def home(request):
    context = {
        'commissions': Commission.objects.all(),
        'title': 'Home'
    }
    return render(request, 'travelingMechanic/home.html', context)

class CommissionListView(CreateView):
    model = Commission
    template_name = 'travelingMechanic/commissions.html'
    fields = ['title', 'description', 'askPrice']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
