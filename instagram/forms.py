from django import forms
from .models import Image

class CreatePost(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','title','caption']
