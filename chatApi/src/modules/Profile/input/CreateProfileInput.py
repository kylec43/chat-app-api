from chatApi.src.framework.classes.InputBase import InputBase
from chatApi.src.classes.validators.Validator import Validator

class CreateProfileInput(InputBase):

    def set(self, data: dict):
        self.username = data['username']
        self.password = data['password']
        self.first_name = data['first_name']
        self.last_name = data['last_name']

    def validate(self):
        return (
            Validator.validate_username(self.username) and 
            Validator.validate_password(self.password) and 
            Validator.validate_first_name(self.first_name) and 
            Validator.validate_last_name(self.last_name)
        )