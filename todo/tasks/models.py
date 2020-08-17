from django.db import models
from django.forms import ModelForm
from django import forms

class Songs(models.Model):
    # song title
    title = models.charField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.charField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)
