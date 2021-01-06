from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields =('brand','model','serial','price','status')

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields =('brand','model','serial','price','status')

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields =('brand','model','serial','price','status')