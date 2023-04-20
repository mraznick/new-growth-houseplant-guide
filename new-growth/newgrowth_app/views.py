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


class OnePlant_ViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, id):
        try:
            plant_results = Plant.objects.get(id=id)
            plant = PlantSerializer(plant_results)
            return Response({'plant': plant.data})
        except:
            return Response({'error': "Sorry, something went wrong"})


class AllPlant_ViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self):
        try:
            results = Plant.objects.all()
            all_plant = PlantSerializer(results, many=True)
            return Response(all_plant.data)
        except:
            return Response({'error': "Something went wrong"})
#  FOR POST MVP - VIEWSET ALLOWING USERS TO ADD PLANTS
#     def post(self, request):
#         try:
#             user = self.request.user
#             isAuthenticated = user.is_authenticated
#             if isAuthenticated:
#                 nickname = request.data['nickname']
#                 latin_name = request.data['latin_name']
#                 img = request.data['img']
#                 window_pref = request.data['window_pref']
#                 drought_tol = request.data['drought_tol']
#                 toxic = request.data['toxic']
#                 userProfile = User_profile.objects.get(user=user)
#                 Plant.objects.create(user=userProfile, nickname=nickname, latin_name=latin_name, img=img, window_pref=window_pref, drought_told=drought_tol, toxic=toxic)
#                 return Response({'message': "Plant successfully added! THank you for your contribution."})
#             else:
#                 return Response({'error': "Not Authenticated - Please make sure you include a token."})
#         except:
#             return Response({'error': "Error: Invalid"})
