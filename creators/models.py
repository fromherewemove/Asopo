from tkinter import CASCADE
from django.db import models
from account.models import User
# Create your models here.

class CreatorFeed(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    profileImg = models.ImageField()
    services = models.ImageField()
    description = models.CharField(max_length = 10000, blank=False, null=False)
    link = models.CharField(max_length=2000)
    link1 = models.CharField(max_length=2000)
    link2 = models.CharField(max_length= 2000)
