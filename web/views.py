from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .models import Like
from .models import Follow

def main(request):
    return render(request, 'web/main.html')


def login(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'web/login.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)


        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            myuser = User.objects.get(username=login_username) 
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(login_password, myuser.password):
                request.session['user'] = myuser.id 
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return render(request, 'web/main.html')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'web/login.html', response_data)

    
def signup(request):
    if request.method == "GET":
        return render(request, 'web/signup.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usercollege = request.POST['usercollege']
        userid = request.POST['userid']
        re_password = request.POST['re_password']
        res_data = {}
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
            return redirect('signup')
        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
            return redirect('signup')
        else :
            user = User(username=username, password=make_password(password), usercollege=usercollege)
            user.save()
        return render(request, 'web/signup.html', res_data)

def alarm(request):
    return render(request, 'web/alarm.html')

def logout(request):
    request.session.pop('user')
    return redirect('/')