from chatApi.src.modules.Profile.services.ServiceFactory import ServiceFactory
from chatApi.src.modules.Profile.input.GetProfileInput import GetProfileInput
from chatApi.src.modules.Profile.input.CreateProfileInput import CreateProfileInput
from chatApi.src.framework.classes.RequestWrapper import RequestWrapper

class ProfileController:

    def __init__(self):
        self.service_factory = ServiceFactory()
        self.profile_service = self.service_factory.ProfileService()

    def create_profile(self, request: RequestWrapper):
        input = CreateProfileInput()
        input.set_from_body(request.get_body())
        
        if not input.validate():
            raise Exception("Invalid input")

        return self.profile_service.create_profile(input.username, input.password, input.first_name, input.last_name)

    def get_profile(self, request: RequestWrapper):
        input = GetProfileInput()
        input.set_from_body(request.get_body())

        if not input.validate():
            raise Exception("Invalid input")

        return self.profile_service.get_profile(input.username)

    def get_all_profiles(self, request: RequestWrapper):
        return self.profile_service.get_all_profiles()
