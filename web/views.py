from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .models import Like
from .models import Follow

def main(request):
    user_pk = request.session.get('user')

    if user_pk:
        user = User.objects.get(pk=user_pk)
        return HttpResponse(user.userid)

    # return HttpResponse("로그인 성공")
    return render(request, 'web/main.html')


def login(request):
    response_data = {}
    check = 0

    if request.method == "GET" :
        return render(request, 'web/login.html')

    elif request.method == "POST":
        login_userid = request.POST.get('userid', None)
        login_password = request.POST.get('password', None)


        if not (login_userid and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            myuser = User.objects.get(userid=login_userid)
            # myuser = auth.authenticate(
            # request, username=username, password=password)
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(login_password, myuser.password):
                # auth.login(request, user)
                request.session['user'] = myuser.id 
                check = 1
                request.session['check'] = check
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                # return redirect('main')
                context = {'check':check}
                return render(request, 'web/main.html', context)
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
            user = User(username=username, password=make_password(password), userid=userid, usercollege=usercollege)
            user.save()
        return render(request, 'web/signup.html', res_data)

def alarm(request):
    return render(request, 'web/alarm.html')

# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         redirect('main')
#     return render(request,'web/login.html')

def logout(request):
    del(request.session['user'])
    # request.session.pop('user')
    return redirect('main')
