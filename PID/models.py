from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# class Role(models.Model):
# 	role = models.CharField(max_length=30)


class Profile(models.Model):
	"""
	Associated to the auth_user in db, One-To-One relation
	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	language = models.CharField(max_length=60)
	# role = models.ForeignKey(Role, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	"""
	Signal sent when a auth_user is created
	:param sender:
	:param instance:
	:param created:
	:param kwargs:
	:return:
	"""
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	"""
	Signal sent when a auth_user is modified
	:param sender:
	:param instance:
	:param kwargs:
	:return:
	"""
	instance.profile.save()


# class User(models.Model):
#     login = models.CharField(max_length=30)
#     password = models.CharField(max_length=255)
#     firstname = models.CharField(max_length=60)
#     lastname = models.CharField(max_length=60)
#     email = models.EmailField(max_length=100)
#     langue = models.CharField(max_length=2)
#     roleId = models.ForeignKey(Role, on_delete=models.CASCADE)


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
	# TODO posteUrl -> poster_url
	posteUrl = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	bookable = models.SmallIntegerField()
	# TODO locationId -> location_id
	locationId = models.ManyToManyField(Location, related_name='show', blank=True)


class Representation(models.Model):
	when = models.DateField
	showId = models.ManyToManyField(Show, related_name='representation', blank=True)
	locationId = models.ManyToManyField(Location, related_name='representation', blank=True)


class RepresentationUser(models.Model):
	places = models.IntegerField()
	representationId = models.ForeignKey(Representation, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


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
