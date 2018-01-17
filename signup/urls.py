from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/$', views.getData, name='signup'),
    #url(r'^signup/$', auth_views.login,{'template_name': 'signup-form/index.html'}, name='signup'),
    #url(r'^home/$', views.home_view, name='account-redirect'),
    url(r'^logout/$', auth_views.logout, name='logout'),

]