from django.utils import timezone
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.decorators import login_required
import smtplib
from .models import *

from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

#AbstraceUser 기반 회원가입
users = User.objects.all()
subject = 'subject'
from_email = 'rlaehgud21764011@gmail.com'

def mailer(users,subject,from_email):
    full_traceback = []
    for user in users:
        to = 'rlaehgud21764011@gmail.com'
        html_content = render_to_string('register_result.html')
        trackback = {}
        try:
            send_mail(subject,strip_tags(html_content), from_email, to, html_message=html_content, fail_silently=False)
            trackback['status'] = True
        except smtplib.SMTPException as e:
            trackback['error'] = '%s (%s)' % (e.message, type(e))
            trackback['status'] = False

        full_traceback.append(trackback)
    errors_to_return = []
    error_not_found = []
    for email in full_traceback:
        if email['status']:
            error_not_found.append(True)
        else:
            error_not_found.append(False)
            errors_to_return.append(email['error'])

    if False in error_not_found:
        error_not_found = False
    else:
        error_not_found = True
    return (error_not_found, errors_to_return)

def mailer_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    subject = 'Subject'
    from_email = 'rlaehgud21764011@gmail.com'
    email_sent, traceback = mailer(user, subject, from_email)

    if email_sent:
        return render(request, 'register_result.html')
    return render(request, 'register.html')

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
            ###mailer_view()
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


