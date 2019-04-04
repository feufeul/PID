from django.db import models


class Artists(models.Model):
    id = models.IntegerField(max_length=255)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

class Types(models.Model):
    id = models.IntegerField(max_length=255)
    type = models.CharField(max_length=60)


class Artist_type(models.Model):
    id = models.IntegerField(max_length=255)
    artist_id = models.IntegerField(max_length=255)
    type_id = models.IntegerField(max_length=255)


class Show(models.Model):
    title = models.CharField(max_length=100)
#    place = models.ForeignKey(Place, on_delete=models.CASCADE)
