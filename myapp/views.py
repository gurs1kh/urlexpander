
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Entry
from .forms import UrlForm
import requests
from bs4 import BeautifulSoup

def url_list(request):
	entries = Entry.objects.order_by('created_date')
	form = UrlForm()
	return render(request, 'urlexpander/url_list.html', {'entries': entries, 'form': form})

def url_add(request):
	form = UrlForm(request.POST)
	if form.is_valid():
		entry = form.save(commit=False)
		r = requests.get(entry.short_url)
		entry.long_url = r.url
		entry.status = r.status_code
		entry.title = BeautifulSoup(r.content).title.text
		entry.save()
	return redirect('myapp.views.url_list')

def url_delete(request, id):
	Entry.objects.get(pk=id).delete()
	return redirect('myapp.views.url_list')
