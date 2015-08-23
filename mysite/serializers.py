from django.forms import widgets
from rest_framework import serializers
from myapp.models import Entry

class EntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Entry
		fields = ('id', 'short_url', 'long_url', 'status', 'title', 'image', 'created_date');
