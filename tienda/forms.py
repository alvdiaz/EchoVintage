from django import forms
from .models import Vinilo, Cassette, Cd
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class ViniloForm(forms.ModelForm):
    
    class Meta:
        model = Vinilo
        fields = '__all__'
        
        widgets = {
            'fecha_lanzamiento':forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }

class CassetteForm(forms.ModelForm):
    
    class Meta:
        model = Cassette
        fields = '__all__'
        
        widgets = {
            'fecha_lanzamiento_cassete':forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }

    
class CdForm(forms.ModelForm):
    
    class Meta:
        model = Cd
        fields = '__all__'
        
        widgets = {
            'fecha_lanzamiento_cd':forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', "first_name", "last_name", "email", "password1", "password2"]
    