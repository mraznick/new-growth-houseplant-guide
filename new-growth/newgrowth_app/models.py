from django.db import models
from django.contrib.auth.models import User


class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=4)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    travel_freq = models.BooleanField
    pets = models.BooleanField
    windows = models.CharField(max_length=50)
    # Need to figure out how to add other user model info in road map

    def __str__(self):
        return self.name


class Plant(models.Model):
    # user = models.ForeignKey(User_profile, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50)
    # Not sure whether this is the correct method
    img = models.URLField(max_length=200)
    window_pref = models.CharField(max_length=50)
    drought_tol = models.BooleanField
    toxic = models.BooleanField
