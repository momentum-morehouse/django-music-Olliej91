from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    release = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.title
