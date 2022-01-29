from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import webUser, review

@receiver(post_save, sender=review)
def update_score(sender, instance, created, **kwargs):
    if created:
        #Update the review score of the web user
        user = instance.target
        star = 0
        count = 0
        for x in review.objects.all().filter(target=user):
            star += x.stars
            count += 1
        instance.target.rating = star/count;
        instance.target.save()


