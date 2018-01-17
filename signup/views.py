
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from signup.forms import SignUpForm

def getData(request):
    if(request.method=='POST'):

        form=SignUpForm(request.POST)
        if(form.is_valid()):
            user=form.save();
            user.refresh_from_db()
            user.save()

            login(request,user)
            return redirect('/home/')
        else:
            return render(request, 'signup-form/index.html', {'form': form})
    else:
        form=SignUpForm()
        return render(request,'signup-form/index.html', {'form': form})




