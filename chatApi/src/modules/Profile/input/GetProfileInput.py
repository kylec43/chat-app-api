from chatApi.src.framework.classes.Input import Input
from chatApi.src.classes.validators.ProfileValidator import ProfileValidator

class GetProfileInput(Input):

    def __init__(self, body):
        self.username = body['username']

    def validate(self):
        return ProfileValidator.validateUsername(self.username)