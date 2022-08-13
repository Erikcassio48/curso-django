from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'pages\home.html', context={
        'name': 'Luiz Otávio',
    })
# Create your views here.
