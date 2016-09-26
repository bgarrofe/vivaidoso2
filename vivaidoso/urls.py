from django.conf.urls import url, include
from . import views
#from django.views.generic.edit import CreateView
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.views import password_reset

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/get_estados/', views.ajax_estados, name='ajax_estados'),
    url(r'^ajax/get_cidades/(?P<estado>[0-9]+)/', views.ajax_cidades, name='ajax_cidades'),
    url(r'^ajax/get_bairros/(?P<cidade>[0-9]+)/', views.ajax_bairros, name='ajax_bairros'),
    url(r'^sobre-nos/$', views.sobre_nos, name='sobre-nos'),
    url(r'^contatos/$', views.contatos, name='contatos'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^avatar/', include('avatar.urls')),
    
]