from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name
