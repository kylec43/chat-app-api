from chatApi.src.framework.classes.InputBase import InputBase
from chatApi.src.classes.validators.Validator import Validator

class CreateProfileInput(InputBase):

    def set_from_body(self, body):
        self.username = body['username']
        self.password = body['password']
        self.first_name = body['first_name']
        self.last_name = body['last_name']

    def validate(self):
        return (
            Validator.validateUsername(self.username) and 
            Validator.validatePassword(self.password) and 
            Validator.validateFirstName(self.first_name) and 
            Validator.validateLastName(self.last_name)
        )