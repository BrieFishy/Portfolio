from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_description = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name

