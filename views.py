from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
def home(request):
    return render(request,'home/Home.html')
def about(request):
    return HttpResponse('<h1>About Page Works!</h1>')
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for %s!'%username)
            return render(request,'home/manage.html')
            print("valid")
        print(form['username'])
        print(form['password'])
    else:
        form=UserRegisterForm()
    return render(request,'home/register.html',{'form':form})
def other(request):
    if request.user.is_authenticated:
        return render(request,'home/discussions.html')
    else:
        return render(request,'home/login.html')
def other1(request):
    if request.user.is_authenticated:
        return render(request,'home/manage.html')
    else:
        return redirect('/login')
