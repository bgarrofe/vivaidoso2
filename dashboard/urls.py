from django.conf.urls import url, include
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import password_reset

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/update/', views.profile_update, name='profile_update'),
    url(r'^prices/analysis_panel/', views.analysis_panel, name='analysis_panel'),
    url(r'^prices/indexes/', views.indexes, name='indexes'),
    url(r'^ajax/get_indexes/', views.ajax_indexes, name='ajax_indexes'),
    url(r'^ajax/get_price_index/(?P<cod>VALE[0-9]{3})/', views.ajax_price_index, name='ajax_price_index'),
    url(r'^prices/composites/', views.composites, name='composites'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^avatar/', include('avatar.urls')),
    
]