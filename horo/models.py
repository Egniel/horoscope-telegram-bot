from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    zodiac_sing = models.CharField(max_length=50)
    date = models.CharField(max_length=50)


class Prediction(models.Model):
    text = models.TextField()
    date = models.CharField(max_length=50)
