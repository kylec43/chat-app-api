from rest_framework.generics import CreateAPIView
from chatApi.src.modules.Profile.services.ServiceFactory import ServiceFactory
from chatApi.src.modules.Profile.input.GetProfileInput import GetProfileInput

class GetProfileView(CreateAPIView):

    def __init__(self, **kwargs: any) -> None:
        super().__init__(**kwargs)
        service_factory = ServiceFactory()
        self.profile_service = service_factory.ProfileService()

    def get(self, request, username):

        data = {
            **request.GET,
            "username": username
        }

        input = GetProfileInput()
        input.set(data)

        if not input.validate():
            raise Exception("Invalid input")

        return self.profile_service.get_profile(input.username)