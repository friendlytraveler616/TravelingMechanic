from django.db import models
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class webUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic = models.ImageField(default='default.png', upload_to='profilePic')
    rating = models.FloatField(default=0,
                                  validators=[validators.MinValueValidator(0), validators.MaxValueValidator(5)])

class Commission(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True)
    lat = models.FloatField(default=-82.374);
    long = models.FloatField(default=29.648);
    askPrice = models.FloatField(default=0, validators=[validators.MinValueValidator(0)])
    images = models.ImageField(default='default.png', upload_to='commissionpic/')
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(webUser, on_delete=models.CASCADE)

    def __str__(self):
        return ('\nTitle: ' + self.title + '\nDescription: ' + self.description
                + '\nAsk price: ' + str(self.askPrice) + '\nUser: ' + self.author.user.username)

    def get_absolute_url(self):
        return reverse('home')

class review(models.Model):
    stars = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(blank=True, upload_to='reviewspic/')
    target = models.ForeignKey(webUser, on_delete=models.CASCADE)
