from django.db import models

"""
This method create a movie model and fields to be stored in the database
- genre: the genre of the movie
- title: title of the movie
- link: link to the movie
- detail: short description of the movie
"""
class Movie(models.Model):
    genre = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField(max_length=300, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    