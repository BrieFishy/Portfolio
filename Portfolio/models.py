from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_description = models.CharField(max_length=100)
    project_image = models.CharField(max_length=2000, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG3aLtQ7Ftn4hPxLlR8MuZt6xARYnsMQo2oA&usqp=CAU')

    def __str__(self):
        return self.project_name


class Hobby(models.Model):
    hobby_name = models.CharField(max_length=50)
    hobby_description = models.CharField(max_length=100)
    hobby_image = models.CharField(max_length=2000, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG3aLtQ7Ftn4hPxLlR8MuZt6xARYnsMQo2oA&usqp=CAU')

    def __str__(self):
        return self.hobby_name

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=200)
    contact_message = models.CharField(max_length=500)

    def __str__(self):
        return self.contact_name

