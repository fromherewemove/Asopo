from django.db import models
from account.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.
class EnduserFeed(models.Model):
    user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE)
    profileImg = models.ImageField(blank=True, null=True)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        EnduserFeed.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+')
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = '+')

class Message(models.Model):
    thread = models.ForeignKey("Thread", related_name='+', on_delete = models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+')
    body = models.CharField(max_length=10000)
    image = models.ImageField(blank=True, null= True)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)