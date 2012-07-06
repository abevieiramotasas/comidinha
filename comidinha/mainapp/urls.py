from django.conf.urls import patterns, url

urlpatterns = patterns('mainapp.views',
    url(r'^$', 'index'),
    url(r'^donorhouse/cadastro/$', 'donor_house_cadastro'),
    url(r'^ip/(?P<ip>.*)$', 'meu_ip'),
    url(r'^donorhouse/$', 'all_donor_houses')
)
