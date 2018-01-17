from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from questionTest.models import FillBlanks, Comprehension, Comparison
from questionTest.models import MultipleMath, SentenceEquivalence, NumericEntry
from django.db import models
from django.contrib.auth.decorators import login_required
from useraccount.models import UserProfile
from django.contrib.auth.models import User
score = 0
count = 0
import random
# Create your views here.
def videosView(request):
    return render(request, 'A_Writing/videos.html')

def mockView(request):
    return render(request, 'questionTemplate/mock.html')


#FillBlanks
@login_required(login_url ='/login/')
def questionView1(request):
    #calculates a random number
    global count

    quest_id_count = FillBlanks.objects.count()
    randomQuesId = random.randint(1, quest_id_count)
    question = FillBlanks.objects.get(id = randomQuesId)
    rightList = [question.option_right1]
    rightList.sort()
    if (request.method == 'POST'):
        list = request.POST.getlist("checkbox[]")
        list.sort()
        if (rightList==list):
            str = "Your ans is correct"
            global score
            score = score + 1
            if(count<20):
                return redirect('/question/2')
            else:
                return redirect('/question/score/')
        str="Wrong ans"
        if (count < 20):
            return redirect('/question/2')
        else:
            return redirect('/question/score/')

    count = count + 1
    return  render(request,'Ques_Template/question1.html', {'question':question})

    #return render(request, 'questionTemplate/question.html' )

#Multiple_Math
@login_required(login_url ='/login/')
def questionView2(request):
    global count

    quest_id_count = MultipleMath.objects.count()
    randomQuesId = random.randint(1, quest_id_count)

    question = MultipleMath.objects.get(id=randomQuesId)
    rightList = [question.option_right1]
    if(question.option_right2 is not None):
        rightList.append(question.option_right2)
    if(question.option_right3 is not None):
        rightList.append(question.option_right3)

    rightList.sort()
    if (request.method == 'POST'):
        list = request.POST.getlist("checkbox[]")
        list.sort()
        if (rightList==list):
            str = "Your ans is correct"
            global score
            score = score + 1
            if (count < 20):
                return redirect('/question/3')
            else:
                return redirect('/question/score/')
        str="Wrong ans"
        if (count < 20):
            return redirect('/question/3')
        else:
            return redirect('/question/score/')
    count = count + 1
    return  render(request,'Ques_Template/question2.html', {'question':question})


#sentence_equivalaance
@login_required(login_url ='/login/')
def questionView3(request):
    global count


    quest_id_count = SentenceEquivalence.objects.count()
    randomQuesId = random.randint(1, quest_id_count)

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
        list = request.POST.getlist("checkbox[]")
        list.sort()
        if (rightList==list):
            str = "Your ans is correct"
            global score
            score = score + 1
            if (count < 20):
                return redirect('/question/4')
            else:
                return redirect('/question/score/')
        str="Wrong ans"
        if (count < 20):
            return redirect('/question/4')
        else:
            return redirect('/question/score/')
    count = count + 1
    return  render(request,'Ques_Template/question3.html', {'question':question})



#numericEntry
@login_required(login_url ='/login/')
def questionView4(request):
    global count


    quest_id_count = NumericEntry.objects.count()
    randomQuesId = random.randint(1, quest_id_count)

    question = NumericEntry.objects.get(id=randomQuesId)
    rightList = [question.option_right_int, question.option_right_frac]

    rightList.sort()
    if (request.method == 'POST'):
        numInt = request.POST['numInt']
        numFrac = request.POST['numFrac']
        list=[numInt, numFrac]

        list.sort()
        if (rightList==list):
            str = "Your ans is correct"
            global score
            score = score + 1
            if (count < 20):
                return redirect('/question/5')
            else:
                return redirect('/question/score/')

        str="Wrong ans"
        if (count < 20):
            return redirect('/question/5')
        else:
            return redirect('/question/score/')
    count = count + 1
    return  render(request,'Ques_Template/question4.html', {'question':question})



#comprehensionn
@login_required(login_url ='/login/')
#comprehension
def questionView5(request):
    global count

    quest_id_count = Comprehension.objects.count()
    randomQuesId = random.randint(1, quest_id_count)

    question = Comprehension.objects.get(id=randomQuesId)
    rightList = [question.option_right1]
    if (question.option_right2 is not None):
        rightList.append(question.option_right2)
    if (question.option_right3 is not None):
        rightList.append(question.option_right3)

    rightList.sort()
    if (request.method == 'POST'):
        list = request.POST.getlist('checkbox[]')


        list.sort()
        if (rightList==list):
            str = "Your ans is correct"
            global score
            score = score + 1
            if (count < 20):
                return redirect('/question/6')
            else:
                return redirect('/question/score/')
        str="Wrong ans"
        if (count < 20):
            return redirect('/question/6')
        else:
            return redirect('/question/score/')
    count = count + 1

    return  render(request,'Ques_Template/question5.html', {'question':question})


#comparison-------
@login_required(login_url ='/login/')
def questionView6(request):
    global count

    quest_id_count = Comparison.objects.count()
    randomQuesId = random.randint(1, quest_id_count)

    question = Comparison.objects.get(id=randomQuesId)
    rightList = [question.option_right1]


    rightList.sort()
    if (request.method == 'POST'):
        list = request.POST.getlist('checkbox[]')


        list.sort()
        if (rightList==list):
            str = "Your ans is correct"
            global score
            score = score + 1
            if (count < 20):
                return redirect('/question/1')
            else:
                return redirect('/question/score/')
        str="Wrong ans"
        if (count < 20):
            return redirect('/question/1')
        else:
            return redirect('/question/score/')
    count = count + 1
    return  render(request,'Ques_Template/question6.html', {'question':question})

@login_required(login_url ='/login/')
def scoreView(request):
    global score
    currentUser = request.user
    id=currentUser.id
    try:
        userPrevious=UserProfile.objects.filter(user_id=id).order_by('-test_no')[0]
        #userPrevious = userPrevious.order_by('test_no')[0]
        prevTestNo = userPrevious.test_no
        prevTestNo = prevTestNo + 1
        newEntry = UserProfile.objects.create(test_no=prevTestNo, score_point=score, user_id=id)
        score2=score
        score=0
    except:
        newEntry = UserProfile.objects.create(test_no=1, score_point=score, user_id=id)
        score2=score
        score = 0

    return render(request, 'Ques_Template/score.html', {'score':score2})