from cli_tool.config import config

def entity_profile_template():
    return f"""from django.db import models
    
class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    column = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return f"{{self.id}} {{self.column}}"
    """


def entity_serializer_profile_template(module_name: str):

    return f"""from rest_framework import serializers
from {config["project_name"]}.src.modules.{module_name}.entities.Profile import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'password', 'first_name', 'last_name']
    """


def entity_serializer_auth_user_template():
    
    return f"""from django.contrib.auth import get_user_model
from rest_framework import serializers


class AuthUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,
                                     style={{'input_type': 'password'}})

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active',)

    def create(self, validated_data: dict):
        user = super(AuthUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    """