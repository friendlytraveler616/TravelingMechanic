from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travelingMechanic.urls')),
    path('user/',include('user.urls')),
    path('payment/', include('payment.urls')),
]

urlpatterns += staticfiles_urlpatterns()