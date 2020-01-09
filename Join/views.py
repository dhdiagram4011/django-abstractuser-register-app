from django.utils import timezone
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.decorators import login_required

#AbstraceUser 기반 회원가입
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
        return render(request, 'Join/register_result.html', {'new_user': new_user})
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



