from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib import auth
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions
# from knox.models import AuthToken
from newgrowth_app.models import User_profile, Plant
from newgrowth_app.serializers import User_profileSerializer, PlantSerializer
