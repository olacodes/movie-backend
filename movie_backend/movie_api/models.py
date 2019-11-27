from django.db import models

# Create your models here.
class Movie(models.Model):
    genre = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField(max_length=300, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    