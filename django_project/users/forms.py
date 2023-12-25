from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:  # ModelForm을 상속하는 클래스는 해당 Model을 Meta class로 설정
        model = User  # sub-class 내의 변수이므로 이름 충돌 없음
        fields = ["username", "email", "password1", "password2"]
