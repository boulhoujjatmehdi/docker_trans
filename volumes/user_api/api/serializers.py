from rest_framework import serializers
from .models import PlayerStates

class PlayerStatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStates
        fields = '__all__'