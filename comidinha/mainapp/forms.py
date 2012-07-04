from models import DonorHouse
#from django.forms import ModelForm
from django.contrib.gis.forms import ModelForm

class DonorHouseCadastro(ModelForm):
    class Meta:
        model = DonorHouse
        exclude = ('address',)
