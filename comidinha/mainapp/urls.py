from django.conf.urls import patterns, url

urlpatterns = patterns('mainapp.views',
    url(r'^$', 'index'),
    url(r'^donorhouse/cadastro/$', 'donor_house_cadastro'),
)
