from chatApi.src.modules.Profile.services.ProfileService import ProfileService

class ServiceFactory:

    def ProfileService(self):
        return ProfileService()
