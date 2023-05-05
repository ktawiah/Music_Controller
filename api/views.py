from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

# Create your views here.


class RoomView(generics.ListCreateAPIView):
    """Endpoint for the Room model"""

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
