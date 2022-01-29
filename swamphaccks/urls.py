from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travelingMechanic.urls')),
    path('user/',include('user.urls')),
    path('payment/', include('payment.urls')),
]
