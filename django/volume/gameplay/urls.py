from django.urls import path 
from . import views

# urlconf
urlpatterns = [
    path('hello/', views.say_hello),
    path('name/', views.say_name)
]
