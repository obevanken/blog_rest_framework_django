from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        result = authenticate(username=data['username'], password=data['password'])
        print(data['username'])
        if result is not None:
            print('none')
            messages.debug(request, ' Username alredy use.')
        else:
            print("зашел")
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            user.save()
            print(user)
            return redirect('/')
    return render(request, "auth/register.html", locals())

def login_auth(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
                print('Зашел')
                login(request, user)
                return redirect('/')
        else:
            print("Зашел 2")
            messages.info(request, ' Неправильный username.')
    return render(request, "auth/login.html", locals())

def logout_auth(request):
    logout(request)
    return redirect("/login")
