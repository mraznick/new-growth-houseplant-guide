from rest_framework import serializers


class UserSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "password": instance.password,
        }
