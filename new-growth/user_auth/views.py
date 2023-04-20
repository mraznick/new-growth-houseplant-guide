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
            user = User.objects.create_user(
                name=name, password=password
            )
            User_profile.objects.create(
                user=user, email=email, name=name
            )
            return Response({
                "success": "Sign up successful",
                # "token": AuthToken.objects.create(user)[1]
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
