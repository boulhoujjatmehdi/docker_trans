from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm, CustomSignupForm
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import PlayerStates
from rest_framework import viewsets
from .serializers import PlayerStatesSerializer

class SimpleAPIView(APIView):
    def get(self, request):
        data = {'message':'hello world from user api'}
        return Response(data)

class PlayerStatesViewSet(viewsets.ModelViewSet):
    queryset = PlayerStates.objects.all()
    serializer_class = PlayerStatesSerializer

def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def custom_signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})
