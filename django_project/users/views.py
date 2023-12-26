from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} 계정 생성됨, 지금부터 로그인 가능")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
