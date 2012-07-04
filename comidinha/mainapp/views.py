# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import DonorHouseCadastro
from django.contrib.gis.utils import GeoIP
import logging

def index(request):
    return render_to_response('index.html', {})

def donor_house_cadastro(request):
    if request.method == 'POST':
        form = DonorHouseCadastro(request.POST)
        remote_ip = request.META['REMOTE_ADDR']
        logging.debug(str(remote_ip))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/donor/')
        else:
            return HttpResponseRedirect('/donor/')
    else:
        form = DonorHouseCadastro()
        c = {}
        c['form'] = form
        c.update(csrf(request))
        return render_to_response('donor_cadastro.html', c)
