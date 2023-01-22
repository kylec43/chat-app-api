from rest_framework.generics import CreateAPIView
from chatApi.src.modules.Profile.services.ServiceFactory import ServiceFactory

class GetAllProfilesView(CreateAPIView):

    def __init__(self, **kwargs: any) -> None:
        super().__init__(**kwargs)
        service_factory = ServiceFactory()
        self.profile_service = service_factory.ProfileService()

    def get(self, request):
        return self.profile_service.get_all_profiles()