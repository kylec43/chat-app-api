from chatApi.src.framework.classes.InputBase import InputBase
from chatApi.src.classes.validators.ProfileValidator import ProfileValidator

class CreateProfileInput(InputBase):

    def set_from_body(self, body):
        self.username = body['username']
        self.password = body['password']
        self.first_name = body['first_name']
        self.last_name = body['last_name']

    def validate(self):
        return ProfileValidator.validateUsername(self.username) and ProfileValidator.validatePassword(self.password) and ProfileValidator.validateFirstName(self.first_name) and ProfileValidator.validateLastName(self.last_name)