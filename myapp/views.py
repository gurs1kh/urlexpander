from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import UrlForm
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from mysite import settings

@login_required(login_url="/urlexpander/login")
def url_list(request):
	entries = Entry.objects.order_by('created_date')
	form = UrlForm()
	return render(request, 'urlexpander/url_list.html', {'entries': entries, 'form': form})

@login_required(login_url="/urlexpander/login")
def url_add(request):
	form = UrlForm(request.POST)
	if form.is_valid():
		entry = form.save(commit=False)
		if not entry.short_url.startswith("http"):
			entry.short_url = "http://" + entry.short_url
		r = requests.get(entry.short_url)
		entry.long_url = r.url
		entry.status = r.status_code
		entry.title = BeautifulSoup(r.content).title.text
		
		driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
		driver.get(entry.short_url)
		filename = entry.title.lower().replace(" ", "-")
		driver.save_screenshot('/tmp/' + filename + '.png')
		driver.close()
		s3 = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
		bucket = s3.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
		key = Key(bucket)
		key.key = '/img/' + filename + '.png'
		key.set_contents_from_filename('/tmp/' + filename + '.png')
		bucket.set_acl('public-read', '/img/' + filename + '.png')
		os.remove('/tmp/' + filename + '.png')
		entry.image = settings.STATIC_URL + "img/" + filename + ".png"
		
		entry.save()
	return redirect('myapp.views.url_list')

@login_required(login_url="/urlexpander/login")
def url_delete(request, id):
	Entry.objects.get(pk=id).delete()
	return redirect('myapp.views.url_list')
