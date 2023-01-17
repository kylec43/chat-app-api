from chatApi.src.framework.classes.InputBase import InputBase
from chatApi.src.classes.validators.ProfileValidator import ProfileValidator

class GetProfileInput(InputBase):

    def set_from_body(self, body):
        self.username = body['username']

    def validate(self):
        return ProfileValidator.validateUsername(self.username)