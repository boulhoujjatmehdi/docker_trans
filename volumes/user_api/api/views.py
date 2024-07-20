from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import PlayerStates
from rest_framework import viewsets
from .serializers import PlayerStatesSerializer

class SimpleAPIView(APIView):
    def get(self, request):
        data = {'message':'hello world'}
        return Response(data)

class PlayerStatesViewSet(viewsets.ModelViewSet):
    queryset = PlayerStates.objects.all()
    serializer_class = PlayerStatesSerializer