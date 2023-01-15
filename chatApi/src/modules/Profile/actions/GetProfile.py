from chatApi.src.classes.Action import Action
from chatApi.src.modules.Profile.services.ProfileService import ProfileService
from chatApi.src.modules.Profile.input.GetProfileInput import GetProfileInput

class GetProfile(Action):

    def __init__(self):
        super().__init__()
        self.service = ProfileService()
        self.input = GetProfileInput()

    def execute(self):
        return self.service.get_profile(self.input.username)

    def validateInput(self):
        return self.input.validate()

    def verifyAccess(self):
        return True
