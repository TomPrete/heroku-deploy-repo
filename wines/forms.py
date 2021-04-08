from django import forms
from .models import Wine

# Here is the Model Form
# Adding a comment here in the forms file
class WineForm(forms.ModelForm):
  class Meta:
    model = Wine
    fields = ['wine_name', 'price', 'varietal', 'description']
