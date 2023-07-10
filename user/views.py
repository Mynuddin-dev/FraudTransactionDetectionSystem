from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
# Create your views here.


# @login_required
# def home(request):
#     context = {

#     }

#     return render(request, 'user/profile.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'user/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


def signup(request):

    if request.method == "POST":
      form = UserRegisterForm(request.POST)
      if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Registration successful." )
        return redirect("signup")
      messages.error(request, "Unsuccessful registration. Invalid information.")

    form = UserRegisterForm()
    return render (request=request, template_name="user/signup.html", context={"form":form})
