from chatApi.src.modules.Profile.entities.AuthUserSerializer import AuthUserSerializer
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

class ProfileService:
    def get_all_profiles(self):
        AuthUser = get_user_model()
        auth_users = AuthUser.objects.all()
        serializer = AuthUserSerializer(auth_users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def get_profile(self, username: str):
        AuthUser = get_user_model()
        auth_user = AuthUser.objects.get(username=username)
        serializer = AuthUserSerializer(auth_user)
        return JsonResponse(serializer.data, safe=False)

    def create_profile(self, data: dict):
        auth_user_serializer = AuthUserSerializer(data=data)
        auth_user_serializer.is_valid(raise_exception=True)
        auth_user_instance = auth_user_serializer.create(data)
        token = Token.objects.create(user=auth_user_instance)
        return JsonResponse({'message': 'success','token': token.key})