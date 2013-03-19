from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.timezone import utc, get_current_timezone
import datetime

class StatusSnapshot(models.Model):
	identity = models.CharField(max_length=55)
	status = models.CharField(max_length=55)

	def __init__(self, identity=None, status=None):
		self.identity = identity
		self.status = status
