# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from TeamAppApi.constants import ROLE_CHOICES

class Team(models.Model):
	"""This class represents the Team model."""

	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	age = models.IntegerField(default=18)
	#role choice could be admin or regular
	role = models.CharField(max_length=100, choices=ROLE_CHOICES)
	phone = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on = models.DateTimeField(auto_now = True)
	#0: Active, 1: Inactive, -1: Deleted
	status = models.IntegerField(default=0)

	def __str__(self):
		"""Return a human readable representation of the model instance."""
		return "{} {} {}".format(self.first_name, self.last_name, self.role)
