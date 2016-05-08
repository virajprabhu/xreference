from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publication(models.Model):
	file_url = models.CharField(max_length=300)
	title = models.CharField(max_length=300)
	author = models.CharField(max_length=200)
	keywords = models.CharField(max_length=300)
	year = models.IntegerField(default=2000)
	venue = models.CharField(max_length=200)
