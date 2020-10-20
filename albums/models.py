from django.db import models

# Create your models here.
class Albums(models.Model):
    album = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    release = models.DateField(null=True, blank=True)
    genre = models.CharField(null=True, blank=True)
    def __str__(self):
        return self.album
