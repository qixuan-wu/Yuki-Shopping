from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password1 != password2:
            msg='Inconsistent passwords'
            return render(request,'create.html')
        elif username == '':
            msg='Username cannot be empty'
            return render(request,'create.html')
        cuser = User.objects.create_user(username=username, password=password1, email=email)
        cuser.save()
        return redirect('login')
    return render(request, 'create.html')


def login_view(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate( username=username, password=password)
            if user :
                login(request, user)
                return redirect('/home')
            else:
                msg='Invalid login credentials'
                return redirect('login')
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('/login')
