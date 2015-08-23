from django.db import models
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from mysite import settings

class Entry(models.Model):
	short_url = models.CharField(max_length=2083)
	long_url = models.CharField(max_length=2083)
	status = models.CharField(max_length=3)
	title = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	image = models.CharField(max_length=2083)
		
	def publish(self):
		if not self.short_url.startswith("http"):
			self.short_url = "http://" + self.short_url
		r = requests.get(self.short_url)
		self.long_url = r.url
		self.status = r.status_code
		self.title = BeautifulSoup(r.content).title.text

		driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
		driver.get(self.short_url)
		filename = self.short_url[7:]
		driver.save_screenshot('/tmp/' + filename + '.png')
		driver.close()
		s3 = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
		bucket = s3.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
		key = Key(bucket)
		key.key = '/img/' + filename + '.png'
		key.set_contents_from_filename('/tmp/' + filename + '.png')
		bucket.set_acl('public-read', '/img/' + filename + '.png')
		os.remove('/tmp/' + filename + '.png')
		self.image = settings.STATIC_URL + "img/" + filename + ".png"
		self.created_date = timezone.now()
		
		self.save()
	
	def __str__(self):
		return self.title
