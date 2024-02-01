from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("notes:home_page")
        else:
            return redirect("users:login")
    else:
        form = UserLoginForm()
        data = {
            "form": form,
        }

        return render(request, "users/login.html", data)


def logout_user(request):
    logout(request)
    return redirect("users:login")


def register(request):
    if request.method == "POST":
        user = UserRegistrationForm(request.POST)

        if user.is_valid():
            user.save()
            return redirect("users:login")
        else:
            form = UserRegistrationForm()
            data = {
                "form": form,
            }

            return render(request, "users/register.html", data)

    else:
        form = UserRegistrationForm()
        data = {
            "form": form,
        }

        return render(request, "users/register.html", data)

