from django.shortcuts import render,redirect
from .forms import UserCreateForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages


def register_view(request):

    if request.method=='POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Successful')
            return redirect('/home/')
        messages.error(request,'Invalid information')
    form = UserCreateForm()

    return render(request,'registration/register.html',context={
        'form':form,
    })

def login_view(request):

    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user != None:
                login(request,user)
                messages.success(request,'Your are logged in {username}')
                return redirect('/home/')
            messages.error(request,'Invalid information')
        messages.error(request,'Invalid information')
    form = AuthenticationForm()

    return render(request,'registration/login.html',context={'form':form})