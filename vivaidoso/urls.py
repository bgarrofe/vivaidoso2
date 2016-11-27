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
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^pesquisar/(?P<cod>\w+)/$', views.pesquisar, name='pesquisar'),
    url(r'^pesquisar/$', views.pesquisar, name='pesquisar'),
    url(r'^dashboard/empresa/(?P<cod>\w+)/', views.empresa, name='empresa'),
    url(r'^dashboard/empresa/', views.empresa, name='empresa'),
    url(r'^ajax/get_empresas/', views.ajax_empresas, name='ajax_empresas'),
    url(r'^ajax/upload_file/(?P<cod>\w+)/', views.ajax_upload_file, name='ajax_upload_file'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/update/', views.profile_update, name='profile_update'),
    url(r'^delete-image/(?P<id>\d+)/$', views.delete_image, name='delete_image'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^avatar/', include('avatar.urls')),
    
]