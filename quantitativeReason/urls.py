from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^quantitative/question/1$', views.quantitativeQuestionView1, name='quantitativeQuestion1'),


]