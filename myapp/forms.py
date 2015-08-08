from django import forms
from .models import Entry

class UrlForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields= ('short_url',)
