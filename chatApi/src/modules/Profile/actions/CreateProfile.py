from chatApi.src.classes.Action import Action
from chatApi.src.modules.Profile.services.ProfileService import ProfileService
from chatApi.src.modules.Profile.input.CreateProfileInput import CreateProfileInput

class CreateProfile(Action):

    def __init__(self):
        super().__init__()
        self.service = ProfileService()
        self.input = CreateProfileInput()

    def execute(self):
        return self.service.create_profile(self.input.username, self.input.password, self.input.first_name, self.input.last_name)

    def validateInput(self):
        return self.input.validate()

    def verifyAccess(self):
        return True