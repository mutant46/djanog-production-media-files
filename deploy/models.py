from django.db import models

# Create your models here.


class MediaFile(models.Model):
    file = models.ImageField()
