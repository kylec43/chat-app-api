from chatApi.src.framework.classes.InputBase import InputBase
from chatApi.src.classes.validators.Validator import Validator

class GetProfileInput(InputBase):

    def set(self, data: dict):
        self.username = data['username']

    def validate(self):
        return Validator.validate_username(self.username)