from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm

def home(request):
    username = None
    if 'user' in request.session:
        user_id = request.session['user']
        user = User.objects.get(id=user_id)
        username = user.username
    return render(request, 'main.html', {'username': username})
    #return render(request, 'main.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}

        if not (username and password):
            res_data['error'] = '모든 값을 입력하세요.'
        else:
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    request.session['user'] = user.id
                    return redirect('/')
                else:
                    res_data['error'] = '비밀번호를 잘못 입력하셨습니다.'
            except User.DoesNotExist:
                res_data['error'] = '아이디가 없습니다.' 
        
        return render(request, 'login.html', res_data)
    
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('pw', None)
        re_password = request.POST.get('pw2', None)

        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력하세요.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        elif User.objects.filter(username=username):
            res_data['error'] = '중복된 아이디가 존재합니다.'
        else:
            user = User(username = username, password = make_password(password))
            user.save()
            return redirect('/user/login/')

        return render(request, 'register.html', res_data)
