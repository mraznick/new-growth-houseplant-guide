from django.db import models
from django.contrib.auth.models import User


class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=4)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    travel_freq = models.BooleanField(('Travels Frequently'), default=False)
    pets = models.BooleanField(('Has Pets'), default=False)
    # Switch to multi-choice checkboxes? Consider how to parse out (convert to array etc)
    windows = models.CharField(
        max_length=50, default='Enter Cardinal Direction')
    # Need to figure out how to add other user model info in road map

    def __str__(self):
        return self.name


class Plant(models.Model):
    # user = models.ForeignKey(User_profile, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50)
    # Not sure whether this is the correct method
    img = models.URLField(max_length=200)
    # Switch to multi-choice checkboxes? Consider how to parse out (convert to array etc)
    window_pref = models.CharField(max_length=50)
    drought_tol = models.BooleanField(('Drought Tolerant'), default=False)
    toxic = models.BooleanField(('Toxic'), default=False)
