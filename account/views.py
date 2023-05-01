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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user('')
            loin(request, user)
            messages.success(request,'successful login')
            return redirect('display_home')
        else:
            msg = 'Invalid login credentials'
            messages.error(request, msg)
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER',reverse('display_home')))
