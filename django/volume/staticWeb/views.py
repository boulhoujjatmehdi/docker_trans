from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    return render (request, 'index.html', {'name':'RACHIDA'})

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
