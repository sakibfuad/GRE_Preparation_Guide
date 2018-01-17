from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from questionTest.models import FillBlanks, Comprehension, Comparison
from questionTest.models import MultipleMath, SentenceEquivalence, NumericEntry
from django.db import models
from django.contrib.auth.decorators import login_required
from useraccount.models import UserProfile
from django.contrib.auth.models import User

@login_required(login_url ='/login/')
def useraccountView(request):
    currentUser = request.user
    id = currentUser.id
    try:
        userPreviousTest = UserProfile.objects.filter(user_id=id).order_by('-test_no')
        return render(request, 'Account_Profile/index.html', {'User': currentUser, 'userPreviousTest': userPreviousTest})

    except:
        #userPreviousTest=[0,0]
        return render(request, 'Account_Profile/index2.html', {'User':currentUser})

# Create your views here.
