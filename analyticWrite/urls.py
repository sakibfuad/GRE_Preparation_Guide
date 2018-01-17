from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^analytical/question/1$', views.analyticalQuestionView1, name='analyticalQuestion1'),
    url(r'^analytical/question/2$', views.analyticalQuestionView2, name='analyticalQuestion2'),

]