import imp
from attr import field
from django import forms
from .models import products

class Pform(forms.ModelForm):
    class Meta:
        model= products
        fields = [ "name","img","price","offer","oldp"]