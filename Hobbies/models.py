from django.db import models


# Create your models here.
class Hobby(models.Model):
    hobby_name = models.CharField(max_length=50)
    hobby_description = models.CharField(max_length=100)

    def __str__(self):
        return self.hobby_name

