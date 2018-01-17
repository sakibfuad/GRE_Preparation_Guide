from django.shortcuts import render
'''
def homepage(request):
    return render(request,"startbootstrap-agency-gh-pages 2/index.html")
'''
from django.http import HttpResponse
from django.template import loader

def homepage(request):
    t = loader.get_template('startbootstrap-agency-gh-pages 2/index.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))