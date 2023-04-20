from rest_framework import serializers
from .models import Plant, User_profile


class User_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_profile
        fields = '__all__'


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'


# class PlantSerializer(serializers.BaseSerializer):
#     def to_representation(self, instance):
#         return {
#             "id": instance.id,
#             # might need to be instance.nick.name
#             "nickname": instance.nickname,
#             "latin name": instance.latin.name,
#             "img": instance.img,
#             "window preference": instance.window.pref,
#             "drought tolerance": instance.drought.tol,
#             "toxic": instance.toxic
#         }
