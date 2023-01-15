from chatApi.src.classes.Action import Action
from chatApi.src.modules.Profile.services.ProfileService import ProfileService

class GetProfileList(Action):

    def __init__(self):
        super().__init__()
        self.service = ProfileService()

    def execute(self):
        return self.service.get_all_profiles()

    def validateInput(self):
        return True

    def verifyAccess(self):
        return True
