from django.db import models
from django.forms import ModelForm
from django import forms

class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)