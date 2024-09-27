from dataclasses import field, fields
from operator import truediv
from pyexpat import model
from typing_extensions import ReadOnly
from django.db import models
from django.dispatch import receiver
from .models import User
from rest_framework import serializers
from .serializers import UserSerializer

class friends(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    class Meta:
        unique_together = ('sender', 'receiver')

    def __str__(self):
        return f"{self.sender} -> {self.receiver} (Accepted: {self.accepted}) (Blocked: {self.blocked})"


class friendsSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    class Meta:
        model = friends
        fields = ['id', 'sender', 'receiver', 'accepted', 'blocked']
    


from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def send_friendship_request(request, target_id):
    try:
        receiver = User.objects.get(id=target_id)
        if request.user == receiver:
            return Response({"error":"you can't send the request to yourself!"}, status=status.HTTP_400_BAD_REQUEST)
        friendship , created = friends.objects.get_or_create(sender = request.user, receiver=receiver)
        if created:
            serializer = friendsSerializer(friendship)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error":"friendship request already sent!"}, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response({"error":"you're not supposed to do that!"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def accept_friendship_request(request, target_id):
    try:
        target = User.objects.get(id = target_id)
        if target == request.user :
            raise Exception("not supposed to do that!")
        friendship = friends.objects.get(sender=target, receiver=request.user, accepted=False)
        friendship.accepted = True
        friendship.save()
        serializer = friendsSerializer(friendship)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except (User.DoesNotExist, Exception):
        return Response({"error":"you're not supposed to do that!"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    pass

def block_user (self, request):
    pass

