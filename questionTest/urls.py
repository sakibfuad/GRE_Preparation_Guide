from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^question/score/$', views.scoreView, name='score'),
    url(r'^videos/$', views.videosView, name='videos'),
    url(r'^mock&practice/$', views.mockView, name='mock'),
    url(r'^question/1$', views.questionView1, name='question1'),
    url(r'^question/2$', views.questionView2, name='question2'),
    url(r'^question/3$', views.questionView3, name='question3'),
    url(r'^question/4$', views.questionView4, name='question4'),
    url(r'^question/5$', views.questionView5, name='question5'),
    url(r'^question/6$', views.questionView6, name='question6'),
    url(r'^question/7$', views.questionView1, name='question7'),
    url(r'^question/8$', views.questionView2, name='question8'),
    url(r'^question/9$', views.questionView3, name='question9'),
    url(r'^question/10$', views.questionView4, name='question10'),
    url(r'^question/11$', views.questionView5, name='question11'),
    url(r'^question/12$', views.questionView6, name='question12'),
    url(r'^question/13$', views.questionView1, name='question13'),
    url(r'^question/14$', views.questionView2, name='question14'),
    url(r'^question/15$', views.questionView3, name='question15'),
    url(r'^question/16$', views.questionView4, name='question16'),
    url(r'^question/16$', views.questionView5, name='question17'),
    url(r'^question/16$', views.questionView6, name='question18'),
    url(r'^question/16$', views.questionView4, name='question19'),
    url(r'^question/16$', views.questionView4, name='question20'),

]