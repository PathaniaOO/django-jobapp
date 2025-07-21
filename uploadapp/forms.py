from django import forms
from .models import Uploads, Uploads2

class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = '__all__'

class UploadForm2(forms.ModelForm):
    class Meta:
        model = Uploads2
        fields = '__all__'