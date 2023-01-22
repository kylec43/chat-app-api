from cli_tool.config import config

def view_create_profile_template(module_name: str):

    return f"""from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from {config["project_name"]}.src.modules.{module_name}.services.ServiceFactory import ServiceFactory
from {config["project_name"]}.src.modules.{module_name}.input.CreateProfileInput import CreateProfileInput

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
    """


def view_get_all_profiles_template(module_name: str):

    return f"""from rest_framework.generics import CreateAPIView
from {config["project_name"]}.src.modules.{module_name}.services.ServiceFactory import ServiceFactory

class GetAllProfilesView(CreateAPIView):

    def __init__(self, **kwargs: any) -> None:
        super().__init__(**kwargs)
        service_factory = ServiceFactory()
        self.profile_service = service_factory.ProfileService()

    def get(self, request):
        return self.profile_service.get_all_profiles()
        """


def view_get_profile_template(module_name: str):

    return f"""from rest_framework.generics import CreateAPIView
from {config["project_name"]}.src.modules.{module_name}.services.ServiceFactory import ServiceFactory
from {config["project_name"]}.src.modules.{module_name}.input.GetProfileInput import GetProfileInput

class GetProfileView(CreateAPIView):

    def __init__(self, **kwargs: any) -> None:
        super().__init__(**kwargs)
        service_factory = ServiceFactory()
        self.profile_service = service_factory.ProfileService()

    def get(self, request, username):

        data = {{
            **request.GET,
            "username": username
        }}

        input = GetProfileInput()
        input.set(data)

        if not input.validate():
            raise Exception("Invalid input")

        return self.profile_service.get_profile(input.username)
    """


def view_factory_template(module_name: str):

    return f"""from chatApi.src.modules.{module_name}.views.CreateProfileView import CreateProfileView
from chatApi.src.modules.{module_name}.views.GetAllProfilesView import GetAllProfilesView
from chatApi.src.modules.{module_name}.views.GetProfileView import GetProfileView

class ViewFactory:

    def CreateProfileView(self, **kwargs):
        return CreateProfileView(**kwargs)

    def GetProfileView(self, **kwargs):
        return GetProfileView(**kwargs)

    def GetAllProfilesView(self, **kwargs):
        return GetAllProfilesView(**kwargs)
    """