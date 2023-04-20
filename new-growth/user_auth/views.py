from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib import auth
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions
from knox.models import AuthToken
from newgrowth_app.models import User_profile, Plant
from newgrowth_app.serializers import User_profileSerializer, PlantSerializer


class SignupView(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        result = User.objects.all()
        all_users = UserSerializer(result, many=True)
        return Response(all_users.data)

    def post(self, request):
        data = self.request.data
        name = data["name"]
        email = data["email"]
        password = data["password"]
        re_password = data["re_password"]
        try:
            if password == re_password:
                user = User.objects.create_user(
                    name=name, password=password
                )
                User_profile.objects.create(
                    user=user, email=email, name=name
                )
                return Response({
                    "success": "Sign up successful",
                    "token": AuthToken.objects.create(user)[1]
                })
        except:
            return Response({"error": "Something went wrong"})


class LoginView(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        data = self.request.data
        username = data["username"]
        password = data["password"]
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return Response({"success": "User Authenticated",
                                "token": AuthToken.objects.create(user)[1]})
            else:
                return Response({"error": "Error Authenticating"})
        except:
            return Response({"error": "Something went wrong while logging in"})


class GrabProfile(APIView):
    def get(self, request):
        try:
            user = self.request.user
            profile = User_profile.objects.get(user=user)
            profile_json = User_profileSerializer(profile)
            plants = Plant.objects.filter(user=plants.id)
            plants_json = PlantSerializer(plants, many=True)
            return Response({"profile": profile_json.data, "plants": plants_json.data})
        except Exception as e:
            print(e)
            return Response({"error": "No user profile found."})
