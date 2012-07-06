# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from forms import DonorHouseCadastro, UserForm
from models import DonorHouse
from django.contrib.gis.utils import GeoIP
from django.core import serializers

def index(request):
    return render_to_response('index.html', {})

def donor_house_cadastro(request):
    if request.method == 'POST':
#        pdb.set_trace()
        form = DonorHouseCadastro(request.POST)
        form_user = UserForm(request.POST)
#        remote_ip = request.META['REMOTE_ADDR']
        remote_ip = '186.213.1.18'
        if form.is_valid() and form_user.is_valid():
            user = form_user.save()
            point = get_point(remote_ip)
            donor_house = DonorHouse(user=user, address=point, **form.cleaned_data)
            donor_house.save()
            return HttpResponseRedirect('/mainapp/')
        else:
            return HttpResponseRedirect('/mainapp/')
    else:
        form = DonorHouseCadastro()
        form_user = UserForm()
        c = {}
        c['form'] = form
        c['form_user'] = form_user
        c.update(csrf(request))
        return render_to_response('cadastro.html', c)
    
def all_donor_houses(request):
    donor_houses = DonorHouse.geo_objects.all()
    retorno = serializers.serialize("json", donor_houses)
    return HttpResponse(retorno, mimetype="text/javascript")
    
def meu_ip(request, ip):
    if request.method == 'GET':
        return HttpResponse("infos : %s" %(get_point(ip)))
    
    
def get_point(ip):
    g = GeoIP()
    remote_location = g.city(ip)
    point = 'POINT(%(lon)s %(lat)s)'
    return point % {'lon': remote_location['longitude'], 'lat': remote_location['latitude']}
