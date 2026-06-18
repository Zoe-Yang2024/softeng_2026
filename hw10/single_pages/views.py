from django.shortcuts import render


def home(request):
    return render(
        request,
        "single_pages/home.html",
        {
            "title": "주조양의 홈",
            "description": "Django로 만든 주조양의 개인 홈페이지",
            "active_page": "home",
        },
    )


def about(request):
    return render(
        request,
        "single_pages/about.html",
        {
            "title": "About Me",
            "description": "스마트팜을 공부하는 주조양의 이야기",
            "active_page": "about",
        },
    )
