from django.shortcuts import render

# Create your views here.
def portfolio_home(request):
    return render(request, "pages/portfolio_home.html", {})

def index(request):
    return render(request, "pages/index.html", {})

def CV(request):
    return render(request, "pages/CV.html", {})

def publications(request):
    return render(request, "pages/publications.html", {})

def ireland_pop_density(request):
    return render(request, "pages/ireland_pop_density.html", {})