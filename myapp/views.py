from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Entry
from .forms import UrlForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mysite.serializers import EntrySerializer
from ratelimit.decorators import ratelimit

def logout_view(request):
	logout(request)
	return redirect('myapp.views.url_list')

@login_required(login_url="/urlexpander/login")
@ratelimit(key='ip', rate='10/m', block=True)
def url_list(request):
	entries = Entry.objects.order_by('created_date')
	form = UrlForm()
	return render(request, 'urlexpander/url_list.html', {'entries': entries, 'form': form})

@login_required(login_url="/urlexpander/login")
@ratelimit(key='ip', rate='10/m', block=True)
def url_add(request):
	form = UrlForm(request.POST)
	if form.is_valid():
		entry = form.save(commit=False)
		entry.publish()		
		entry.save()
	return redirect('myapp.views.url_list')

@login_required(login_url="/urlexpander/login")
@ratelimit(key='ip', rate='10/m', block=True)
def url_delete(request, id):
	Entry.objects.get(pk=id).delete()
	return redirect('myapp.views.url_list')

@login_required(login_url="/urlexpander/login")
@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET'])
def api_list(request, format=None):
	entries = Entry.objects.all()
	serializer = EntrySerializer(entries, many=True)
	return Response(serializer.data)

@login_required(login_url="/urlexpander/login")
@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET'])
def api_details(request, id, format=None):
	try:
		entry = Entry.objects.get(pk=pk)
	except Entry.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = EntrySerializer(entry)
	return Response(serializer.data)

@login_required(login_url="/urlexpander/login")
@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET'])
def api_delete(request, id):
	Entry.objects.get(pk=id).delete()
	return redirect('api_list')

@login_required(login_url="/urlexpander/login")
@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['POST'])
def api_add(request):
	form = UrlForm(request.data)
	if form.is_valid():
		entry = form.save(commit=False)
		entry.publish()
		entry.save()
	serializer = EntrySerializer(entry)
	return Response(serializer.data)

@login_required(login_url="/urlexpander/login")
@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET'])
def api_update(request, id):
	try:
		entry = Entry.objects.get(pk=id)
	except Entry.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	entry.publish()
	serializer = EntrySerializer(entry)
	return Response(serializer.data)

