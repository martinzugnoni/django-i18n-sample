from django.shortcuts import render
from core.models import HomePage, AboutPage

def home_page(request):
    # print('>>>>>>', request.LANGUAGE_CODE)
    homepage = HomePage.objects.first()
    return render(request, 'page.html', context={'page': homepage})


def about_page(request):
    aboutpage = AboutPage.objects.first()
    return render(request, 'page.html', context={'page': aboutpage})
