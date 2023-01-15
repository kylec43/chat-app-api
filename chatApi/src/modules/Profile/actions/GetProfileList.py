from chatApi.src.framework.classes.Action import Action
from chatApi.src.modules.Profile.services.ProfileService import ProfileService

class GetProfileList(Action):
    
    def execute(self):
        service = ProfileService()
        return service.get_all_profiles()

    def validateInput(self):
        return True

    def verifyAccess(self):
        return True
