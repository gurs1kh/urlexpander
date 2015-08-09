from django import forms
from .models import Entry

class UrlForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ('short_url',)
		widgets = {
			'short_url': forms.TextInput(attrs={
				'type':'text',
				'id':'url-input',
				'name':'url-input',
				'placeholder':'http://...',
				'class':'form-control input-md',
			}),
		}
