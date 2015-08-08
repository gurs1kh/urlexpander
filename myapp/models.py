from django.db import models
from django.utils import timezone


class Entry(models.Model):
	short_url = models.CharField(max_length=2083)
	long_url = models.CharField(max_length=2083)
	status = models.CharField(max_length=3)
	title = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	
	def publish(self):
		self.save()
	
	def __str__(self):
		return self.title
