from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly  
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

from .models import PlayerModel 
from .serializers import PlayerSerializer 

class PlayerViewSet(viewsets.ModelViewSet):
    queryset=PlayerModel.objects.all()
    serializer_class=PlayerSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle, UserRateThrottle]

#Super_user user and pass : Subham    
