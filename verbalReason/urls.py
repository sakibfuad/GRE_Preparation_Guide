from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^verbal/question/1$', views.verabalQuestionView1, name='verbalQuestion1'),
    url(r'^verbal/question/2$', views.verabalQuestionView2, name='verbalQuestion2'),
    url(r'^verbal/question/3$', views.verabalQuestionView3, name='verbalQuestion3'),
]