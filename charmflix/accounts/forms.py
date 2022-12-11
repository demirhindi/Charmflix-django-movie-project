from django import forms
from .models import Customer

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['avatar']
