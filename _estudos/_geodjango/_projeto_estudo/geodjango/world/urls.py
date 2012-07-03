from django.conf.urls import url, patterns


urlpatterns = patterns('world.views',
   url(r'^$', 'index')
)
