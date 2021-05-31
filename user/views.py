from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .models import User

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password ):
            res_data['error'] = '모든 입력값을 입력해야 합니다.'
        else:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # 비밀번호 일치, 로그인 성공
                pass
            else:
                res_data['error'] = '비밀번호가 일치하지 않습니다.'

        return render(request, 'login.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 입력값을 입력해야 합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호와 비밀번호 확인이 일치하지 않습니다!'
        else:
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            user.save()

        return render(request, 'register.html', res_data)

