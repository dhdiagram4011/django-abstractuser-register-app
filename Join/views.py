from django.utils import timezone
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.decorators import login_required
import smtplib
from .models import *


#AbstraceUser 기반 회원가입
def mailer():
    sender = smtplib.SMTP('smtp.gmail.com', 587)
    sender.starttls()
    sender.login("rlaehgud21764011@gmail.com", "08425256@kdh")
    message = "Register Complete"
    sender.sendmail("rlaehgud21764011@gmail.com", "rlaehgud21764011@gmail.com", message)
    sender.quit()


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            userlists = User.objects.all().order_by('-id')[:1]
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            mailer()
        return redirect('RegisterResult')
    else:
        form = UserForm()
        return render(request, 'Join/register.html', {'form':form})


@login_required()
def login_success(request):
    return render(request, 'Join/login_success.html')


@login_required()
def Userlist(request):
    userlists = User.objects.all()
    return render(request, 'Join/userlist.html', {'userlists':userlists})


def RegisterResult(request):
    userlists = User.objects.all().order_by('-id')[:1]
    return render(request, 'Join/register_result.html', {'userlists':userlists})


