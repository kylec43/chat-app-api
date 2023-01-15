from chatApi.src.modules.Profile.entities.Profile import Profile
from chatApi.src.modules.Profile.entities.ProfileSerializer import ProfileSerializer
from django.http import JsonResponse

class ProfileService:
    def get_all_profiles(self):
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def get_profile(self, username):
        user = Profile.objects.get(username=username)
        serializer = ProfileSerializer(user)
        return JsonResponse(serializer.data, safe=False)

    def create_profile(self, username, password, first_name, last_name):
        profile = Profile(username=username, password=password, first_name=first_name, last_name=last_name)
        profile.save()
        return JsonResponse({'message': 'success'})