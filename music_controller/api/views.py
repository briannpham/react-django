from django.shortcuts import render
from rest_framework import generics     # create a class inherited from generics class
from .models import Room
from .serializers import RoomSerializer

# Create your views here.

# this is where you write your endpoints 
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
