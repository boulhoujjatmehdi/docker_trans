from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def say_hello(request):
    return HttpResponse("hello mothertrucker")
def say_name(request):
    return render(request, 'hello.html', {'name':'mehdi'})