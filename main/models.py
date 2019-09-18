from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class experience(models.Model):
    title = models.CharField(max_length=40)
    date = models.CharField(max_length=40)
    content = models.TextField()
    def __str__(self):
        return self.title