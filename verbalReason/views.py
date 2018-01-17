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

@login_required(login_url ='/login/')
def verabalQuestionView1(request):
    #calculates a random number
    if(request.method == 'GET'):
        quest_id_count = FillBlanks.objects.count()
        randomQuesId = random.randint(1, quest_id_count)
        global currentQuestionID
        currentQuestionID = randomQuesId
        question = FillBlanks.objects.get(id = randomQuesId)
        rightList = [question.option_right1]
        rightList.sort()
    if (request.method == 'POST'):
        question = FillBlanks.objects.get(id=currentQuestionID)
        rightList = [question.option_right1]
        rightList.sort()
        list = request.POST.getlist("checkbox[]")
        list.sort()
        if (rightList==list):
            str = "Your answer is correct!!!"
            return render(request, 'V_Reasoning/vquestion1.html', {'question': question, 'str':str , 'rightList':rightList})

        str="Your answer is wrong!!!"
        return render(request, 'V_Reasoning/vquestion1.html', {'question': question, 'str':str, 'rightList':rightList})

    return  render(request,'V_Reasoning/vquestion1.html', {'question':question})

    #return render(request, 'questionTemplate/question.html' )

#sentence equivalance
@login_required(login_url ='/login/')
def verabalQuestionView2(request):
    if (request.method == 'GET'):
        quest_id_count = SentenceEquivalence.objects.count()
        randomQuesId = random.randint(1, quest_id_count)
        global currentQuestionID
        currentQuestionID = randomQuesId
        question = SentenceEquivalence.objects.get(id=randomQuesId)
        rightList = [question.option_right1]
        if(question.option_right2 is not None):
            rightList.append(question.option_right2)
        if(question.option_right3 is not None):
            rightList.append(question.option_right3)
        if (question.option_right4 is not None):
            rightList.append(question.option_right4)
        if (question.option_right5 is not None):
            rightList.append(question.option_right5)

        rightList.sort()
    if (request.method == 'POST'):
        question = SentenceEquivalence.objects.get(id=currentQuestionID)
        rightList = [question.option_right1]
        if (question.option_right2 is not None):
            rightList.append(question.option_right2)
        if (question.option_right3 is not None):
            rightList.append(question.option_right3)
        if (question.option_right4 is not None):
            rightList.append(question.option_right4)
        if (question.option_right5 is not None):
            rightList.append(question.option_right5)

        rightList.sort()

        list = request.POST.getlist("checkbox[]")
        list.sort()
        if (rightList==list):
            str = "Your answer is correct!!!"

            return render(request, 'V_Reasoning/vquestion2.html', {'question': question, 'str':str , 'rightList':rightList})

        str="Your answer is wrong !!!"
        return render(request, 'V_Reasoning/vquestion2.html', {'question': question, 'str':str , 'rightList':rightList})

    return  render(request,'V_Reasoning/vquestion2.html', {'question':question})



#comprehensionn
@login_required(login_url ='/login/')
#comprehension
def verabalQuestionView3(request):
    if (request.method == 'GET'):
        quest_id_count = Comprehension.objects.count()
        randomQuesId = random.randint(1, quest_id_count)
        global currentQuestionID
        currentQuestionID = randomQuesId
        question = Comprehension.objects.get(id=randomQuesId)
        rightList = [question.option_right1]
        if (question.option_right2 is not None):
            rightList.append(question.option_right2)
        if (question.option_right3 is not None):
            rightList.append(question.option_right3)

        rightList.sort()
    if (request.method == 'POST'):
        question = Comprehension.objects.get(id=currentQuestionID)
        rightList = [question.option_right1]
        if (question.option_right2 is not None):
            rightList.append(question.option_right2)
        if (question.option_right3 is not None):
            rightList.append(question.option_right3)

        rightList.sort()
        list = request.POST.getlist('checkbox[]')


        list.sort()
        if (rightList==list):
            str = "Your ans is correct!!!"

            return render(request, 'V_Reasoning/vquestion3.html', {'question': question, 'str':str , 'rightList':rightList})

        str="Your ans is Wrong!!!"
        return render(request, 'V_Reasoning/vquestion3.html', {'question': question, 'str':str , 'rightList':rightList})

    return  render(request,'V_Reasoning/vquestion3.html', {'question':question})

