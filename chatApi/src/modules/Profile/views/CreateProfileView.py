from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from chatApi.src.modules.Profile.services.ServiceFactory import ServiceFactory
from chatApi.src.modules.Profile.input.CreateProfileInput import CreateProfileInput

class CreateProfileView(CreateAPIView):
    permission_classes = [AllowAny]

    def __init__(self, **kwargs: any) -> None:
        super().__init__(**kwargs)
        service_factory = ServiceFactory()
        self.profile_service = service_factory.ProfileService()

    def create(self, request):
        input = CreateProfileInput()
        input.set(request.POST)
        
        if not input.validate():
            raise Exception("Invalid input")

        return self.profile_service.create_profile(input.to_dict())
