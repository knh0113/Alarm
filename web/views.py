from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User
from .models import Like
from .models import Follow

def main(request):
    return render(request, 'web/main.html')


def login(request):
    return render(request, 'web/login.html')

    
def signup(request):
    if request.method == "GET":
        return render(request, 'web/signup.html')

    elif request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        usercollege = request.POST.get['usercollege']
        re_password = request.POST.get['re_password']
        res_data = {}
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            user = User(username=username, password=make_password(password), usercollege=usercollege)
            user.save()
        return render(request, 'web/signup.html', res_data)

def alarm(request):
    return render(request, 'web/alarm.html')
