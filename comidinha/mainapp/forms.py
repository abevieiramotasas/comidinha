from models import DonorHouse
#from django.forms import ModelForm
from django.contrib.gis.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {'password': PasswordInput}

class DonorHouseCadastro(ModelForm):   
    class Meta:
        model = DonorHouse
        exclude = ('address','user')
