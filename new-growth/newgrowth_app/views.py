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


class User_Profile_Update_ViewSet(APIView):
    def put(self, request, id):
        try:
            user = self.request.user
            isAuthenticated = user.is_authenticated
            if isAuthenticated:
                name = request.data['name']
                email = request.data['email']
                travel_freq = request.data['travel_freq']
                pets = request.data['pets']
                windows = request.data['windows']
                # May need to rework following lines
                reqProfile = User_profile.objects.get(user=user)
                logProfile = User_profile.objects.get(id=id)
                userProfile = reqProfile.id
                loggedProfile = logProfile.id
                print(userProfile)
                print(loggedProfile)
                if loggedProfile == userProfile:
                    User_profile.objects.update(
                        name=name, email=email, travel_freq=travel_freq, pets=pets, windows=windows)
                    return Response({'message': "Profile updated successfully."})
                else:
                    return Response({'message': "You are not authorized to perform this action."})
            else:
                return Response({'error': "Not Authenticated - Please make sure you include a token."})
        except:
            return Response({'error': "Error: Invalid"})
