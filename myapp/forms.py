from django import forms
from .models import contacts

class ContactForm(forms.ModelForm):
          class Meta:
                  model= contacts
                  fields= ['name','email','message']