import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Venues(models.Model):
	name = models.CharField(max_length=200)
	added = models.DateTimeField('date published')
	url = models.URLField( max_length=128, db_index=True, unique= True,  blank=False)
	email = models.EmailField(max_length=70,blank=True, unique= True)
	price = models.IntegerField(blank = True, null = True)
	tables = models.BooleanField(default=False)
	cutlery = models.BooleanField(default=False)
	crockery = models.BooleanField(default=False)
	accomodation = models.BooleanField(default=False)

	def __str__(self):
		"""Return a human readable representation of the model instance."""
		return "{}".format(self.name)
