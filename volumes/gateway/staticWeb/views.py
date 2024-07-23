from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError
from django.template.loader import render_to_string
from rest_framework.response import Response
import requests

# Create your views here.
def index(request):
    return render (request, 'index.html', {'name':'RACHIDAa'})

def home(request):
    string = render_to_string('sections/home.html')
    css = 'static/css/home.css'
    js = ''
    return JsonResponse({'content':string, 'css':css, 'js':js})

def game(request):
    string = render_to_string('sections/game.html')
    css = 'static/css/game.css'
    js = 'static/js/racket-mv.js'
    return JsonResponse({'content': string, 'css':css, 'js':js})


def login(request):
    url = 'http://userapi:8000/api/simple/'

    response = requests.get(url)
    if response.status_code == 201:
        data = response.json()
        return JsonResponse(data)
    else:
        return HttpResponseServerError('Failed To Fetch Data')
    return render(request, 'login.html')
        