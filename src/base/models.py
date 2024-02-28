from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class UserProfile(models.Model):
    email = models.EmailField()
    username = models.ForeignKey(User, on_delete=CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Posts(models.Model):
    username = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=100)
    image = models.ImageField()
    caption = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)

