from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=30)


class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    langue = models.CharField(max_length=2)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)


class Localitie(models.Model):
    pass
    # primary key postal_code
    # primary key locality
    # primary key locality_id


class Location(models.Model):
    # primary key slug
    designation = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    website = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    localityId = models.OneToOneField(Localitie, on_delete=models.CASCADE)


class Show(models.Model):
    # primary key slug
    title = models.CharField(max_length=255)
    posteUrl = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bookable = models.SmallIntegerField()
    locationId = models.ManyToManyField(Location, related_name='show', blank=True)


class Representation(models.Model):
    when = models.DateField
    showId = models.ManyToManyField(Show, related_name='representation', blank=True)
    locationId = models.ManyToManyField(Location, related_name='representation', blank=True)


class RepresentationUser(models.Model):
    places = models.IntegerField()
    representationId = models.ForeignKey(Representation, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class Artist(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)


class Type(models.Model):
    type = models.CharField(max_length=60)


class ArtisteType(models.Model):
    artistId = models.ForeignKey(Artist, on_delete=models.CASCADE)
    typeId = models.ForeignKey(Type, on_delete=models.CASCADE)


class ArtisteTypeShow(models.Model):
    artisteTypeId = models.ForeignKey(ArtisteType, on_delete=models.CASCADE)
    showId = models.ForeignKey(Show, on_delete=models.CASCADE)
