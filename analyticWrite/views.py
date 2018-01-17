from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from questionTest.models import FillBlanks, Comprehension, Comparison
from questionTest.models import MultipleMath, SentenceEquivalence, NumericEntry
from django.db import models
from django.contrib.auth.decorators import login_required
from useraccount.models import UserProfile
from django.contrib.auth.models import User
currentQuestionID = 0
questionCount=0
import random

#Multiple_Math
@login_required(login_url ='/login/')
def analyticalQuestionView1(request):
    if (request.method == 'GET'):
        quest_id_count = MultipleMath.objects.count()
        randomQuesId = random.randint(1, quest_id_count)
        global currentQuestionID
        currentQuestionID = randomQuesId
        question = MultipleMath.objects.get(id=randomQuesId)
        rightList = [question.option_right1]
        if(question.option_right2 is not None):
            rightList.append(question.option_right2)
        if(question.option_right3 is not None):
            rightList.append(question.option_right3)

        rightList.sort()
    if (request.method == 'POST'):
        question = MultipleMath.objects.get(id=currentQuestionID)
        rightList = [question.option_right1]
        if (question.option_right2 is not None):
            rightList.append(question.option_right2)
        if (question.option_right3 is not None):
            rightList.append(question.option_right3)

        rightList.sort()
        list = request.POST.getlist("checkbox[]")
        list.sort()
        if (rightList==list):
            str = "Your ans is correct!!!"
            return render(request, 'A_Writing/index.html', {'question': question, 'str':str, 'rightList':rightList})

        str="Your ans is wrong!!!"
        return render(request, 'A_Writing/index.html', {'question': question, 'str':str, 'rightList':rightList})

    return  render(request,'A_Writing/index.html', {'question':question})


#numericEntry
@login_required(login_url ='/login/')
def analyticalQuestionView2(request):
    if (request.method == 'GET'):

        quest_id_count = NumericEntry.objects.count()
        randomQuesId = random.randint(1, quest_id_count)
        global currentQuestionID
        currentQuestionID = randomQuesId

        question = NumericEntry.objects.get(id=randomQuesId)
        rightList = [question.option_right_int, question.option_right_frac]

        #rightList.sort()
    if (request.method == 'POST'):
        question = NumericEntry.objects.get(id=currentQuestionID)
        rightList = [question.option_right_int, question.option_right_frac]

        #rightList.sort()
        numInt = request.POST['numInt']
        numFrac = request.POST['numFrac']
        list=[numInt, numFrac]

        #list.sort()
        if (rightList==list):
            str = "Your ans is correct!!!"
            global score
            score = score + 1
            return render(request, 'A_Writing/index1.html', {'question': question, 'str':str, 'rightList':rightList})

        str="Your ans is wrong!!!"
        return render(request, 'A_Writing/index1.html', {'question': question, 'str':str, 'rightList':rightList})

    return  render(request,'A_Writing/index1.html', {'question':question})


