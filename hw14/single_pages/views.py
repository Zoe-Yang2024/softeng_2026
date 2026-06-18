from django.shortcuts import render


def landing(request):
    return render(request, "single_pages/landing.html")


def about(request):
    skills = ["Python", "Flask", "Django", "HTML & CSS"]
    return render(request, "single_pages/about.html", {"skills": skills})
