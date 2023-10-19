from django.shortcuts import render, redirect
from .auth import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
def home(request):
    return render(request,"frontend/home.html")

def signup(request):
        form = RegisterForm()
        if request.method == "POST":
                print(request.POST)
                form = RegisterForm(request.POST)
                if form.is_valid():
                        new_user = form.save()
                        new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
                        userobj = User.objects.get(username=form.cleaned_data['username'])
                        token = Token.objects.create(user=userobj)
                        print("wallah.: ",token)
                        login(request, new_user)
                        return redirect('/')
                else:
                        errmsg = "Check Your Credentials"
        return render(request, 'frontend/signup.html', {"Createform": form})

def signin(request):
    if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        return redirect('/')
                else:
                        context = {'err': "Your Username or password is incorrect"}
                        return render(request, 'frontend/signin.html', context)
    return render(request,"frontend/signin.html")

def logoutuser(request):
        logout(request)
        return HttpResponseRedirect('/home/')

@login_required(login_url='/home/')
def userpage(request):
    token_id={'token': Token.objects.get(user_id=request.user.id)}
    return render(request,"frontend/main.html",token_id)

