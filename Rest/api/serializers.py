from rest_framework import serializers 
from .models import PlayerModel

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=PlayerModel 
        fields=('playerName','jerseyNumber','url','country')
