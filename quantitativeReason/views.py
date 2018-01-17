from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from questionTest.models import FillBlanks, Comprehension, Comparison
from questionTest.models import MultipleMath, SentenceEquivalence, NumericEntry
from django.db import models
from django.contrib.auth.decorators import login_required
from useraccount.models import UserProfile
from django.contrib.auth.models import User
import random
score =0
currentQuestionID=0
# Create your views here.
# Create your views here.
#comparison-------
@login_required(login_url ='/login/')
def quantitativeQuestionView1(request):

    if(request.method == 'GET'):
        quest_id_count = Comparison.objects.count()
        randomQuesId = random.randint(1, quest_id_count)
        global currentQuestionID
        currentQuestionID = randomQuesId

        question = Comparison.objects.get(id=randomQuesId)
        rightList = [question.option_right1]

        rightList.sort()
    if (request.method == 'POST'):

        question = Comparison.objects.get(id=currentQuestionID)
        rightList = [question.option_right1]
        rightList.sort()
        list = request.POST.getlist('checkbox[]')
        list.sort()
        if (rightList==list):
            str = "Your answer is correct!!!"
            return render(request, 'Q_Reasoning/index.html', {'question': question, 'str':str, 'rightList':rightList})
        str="Your answer is wrong!!!"
        return render(request, 'Q_Reasoning/index.html', {'question': question, 'str':str, 'rightList':rightList})

    return  render(request,'Q_Reasoning/index.html', {'question':question})
