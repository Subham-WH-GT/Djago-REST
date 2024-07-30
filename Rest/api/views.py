from django.shortcuts import render
from rest_framework import viewsets 

from .models import PlayerModel 
from .serializers import PlayerSerializer 

class PlayerViewSet(viewsets.ModelViewSet):
    queryset=PlayerModel.objects.all()
    serializer_class=PlayerSerializer

#Super_user user and pass : Subham    
