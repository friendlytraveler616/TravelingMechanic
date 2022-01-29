from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Commission(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    askPrice = models.IntegerField
    images = models.ImageField
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)