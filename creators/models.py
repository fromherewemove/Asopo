from tkinter import CASCADE
from django.db import models
from account.models import User
from django.utils import timezone
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
class Post(models.Model):
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

class CreatorFeed(models.Model):
    user = models.OneToOneField(User, primary_key = True, verbose_name = 'user', related_name='profile',on_delete=models.CASCADE)
    name = models.CharField(max_length=3000, blank=True, null=True)
    profileImg = models.ImageField(blank=True, null=True)
    services = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length = 10000, blank=True, null=True)
    link = models.CharField(max_length=2000, blank=True, null=True)
    link1 = models.CharField(max_length=2000, blank=True, null=True)
    link2 = models.CharField(max_length= 2000, blank=True, null=True)
    followers = models.ManyToManyField(User, blank=True, related_name= 'followers')

        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CreatorFeed.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()