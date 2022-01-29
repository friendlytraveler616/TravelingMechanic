from django.db import models
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.
class Commission(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=False)
    lat = models.IntegerField(default=-82.374);
    long = models.IntegerField(default=29.648);
    askPrice = models.IntegerField(default=0, validators=[validators.MinValueValidator(0)])
    images = models.ImageField(default='default.png', upload_to='commissionpic/')
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ('\nTitle: ' + self.title + '\nDescription: ' + self.description
                + '\nAsk price: ' + str(self.askPrice) + '\nUser: ' + self.author.username)

# class webUser(User):
#     class
