from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        "author": "이동현",
        "title": "글 1",
        "content": "첫번째 글",
        "date_posted": "2023-12-22",
    },
    {
        "author": "홍길동",
        "title": "글 2",
        "content": "두번째 글",
        "date_posted": "2023-12-32",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
