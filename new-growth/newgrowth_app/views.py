from rest_framework import viewsets
from .models import User_profile, Plant
from rest_framework.views import APIView
from .serializers import User_profileSerializer, PlantSerializer
from rest_framework import permissions
from rest_framework.response import Response


class UserProfile_ViewSet(viewsets.ModelViewSet):
    queryset = User_profile.objects.all()
    serializer_class = User_profileSerializer


class Plant_ViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
