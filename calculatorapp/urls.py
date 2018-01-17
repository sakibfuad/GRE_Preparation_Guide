from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^calculator/', views.index, name='index')
]
