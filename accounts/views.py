from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                messages.info(request, "Thanks for registering. You are now logged in.")
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        )
                login(request, new_user)
                return redirect('tasks:home')
        else:
            return render(request , 'accounts/signup.html')
    else:
        return redirect("tasks:home")

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks:home')
            else:
                return render(request, 'accounts/login.html')


        else:
            return render(request, 'accounts/login.html')
    else:
        return redirect('tasks:home')


def logout_user(request):
    logout(request)
    return redirect('tasks:home')
