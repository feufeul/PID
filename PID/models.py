from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Place(models.Model):
    name = models.CharField(max_length=100)


class Show(models.Model):
    title = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
