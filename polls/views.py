from django.shortcuts import render
from rest_framework.response import Response
from .models import GameModel
from .serializers import GameSerializers
from rest_framework import generics
# Create your views here.

class GetGame(generics.ListAPIView):
      queryset = GameModel.objects.all()
      serializer_class = GameSerializers

class CreateGame(generics.CreateAPIView):
      queryset = GameModel.objects.all()
      serializer_class = GameSerializers
    
class GetCreateGame(generics.ListCreateAPIView):
      queryset = GameModel.objects.all()
      serializer_class = GameSerializers

class DetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
      queryset = GameModel.objects.all()
      serializer_class = GameSerializers