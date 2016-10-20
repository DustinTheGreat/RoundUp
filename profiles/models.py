from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
	user = models.ForeignKey(User)
	profile_picture = models.CharField(max_length=1000)
	location = models.CharField(max_length=100) 
	rating = models.IntegerField(null=True, blank=True)
	transactions = models.IntegerField(null=True, blank=True)


	def __str__(self):
		return self.user.username

# Create your models here.
