from django.shortcuts import render


def index(request):
    return render(request, 'core_app/main_page.html')


def about(request):
    return render(request, 'core_app/about_page.html')
