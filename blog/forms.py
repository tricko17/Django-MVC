from django import forms
from .models import Post

class FormPost(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'

class FormPostDelete(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['slug',]
		exclude = '__all__'
