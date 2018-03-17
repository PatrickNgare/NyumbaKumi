
from django import forms
from .models import User_profile
class EditProfile(forms.ModelForm):
    
    class Meta:
        model = User_profile
        fields = ['name', 'email']
    

