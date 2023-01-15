from chatApi.src.framework.classes.Action import Action
from chatApi.src.modules.Profile.services.ProfileService import ProfileService
from chatApi.src.modules.Profile.input.GetProfileInput import GetProfileInput

class GetProfile(Action):

    def setInput(self, body):
        self.input = GetProfileInput(body)

    def execute(self):
        service = ProfileService()
        return service.get_profile(self.input.username)

    def validateInput(self):
        return self.input.validate()

    def verifyAccess(self):
        return True
