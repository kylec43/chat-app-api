from chatApi.src.framework.classes.Action import Action
from chatApi.src.modules.Profile.services.ProfileService import ProfileService
from chatApi.src.modules.Profile.input.CreateProfileInput import CreateProfileInput

class CreateProfile(Action):

    def setInput(self, body):
        self.input = CreateProfileInput(body)
        
    def validateInput(self):
        return self.input.validate()

    def verifyAccess(self):
        return True

    def execute(self):
        service = ProfileService()
        return service.create_profile(self.input.username, self.input.password, self.input.first_name, self.input.last_name)