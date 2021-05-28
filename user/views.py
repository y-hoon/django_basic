from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        if password != re_password:
            return HttpResponse('비밀번호와 비밀번호 확인이 일치하지 않습니다!')

        user = User(
            username=username,
            password=password
        )

        user.save()

        return render(request, 'register.html')

