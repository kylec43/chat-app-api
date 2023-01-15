from rest_framework import serializers
from chatApi.src.modules.Profile.entities.Profile import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'password', 'first_name', 'last_name']