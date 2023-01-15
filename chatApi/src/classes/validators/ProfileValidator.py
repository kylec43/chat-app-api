from chatApi.src.classes.validators.Validator import Validator

class ProfileValidator:

    @staticmethod
    def validateUsername(username):
        return Validator.validateLength(username, 0, 50)

    @staticmethod
    def validatePassword(password):
        return Validator.validateLength(str(password), 0, 50)

    @staticmethod
    def validateFirstName(first_name):
        return Validator.validateLength(first_name, 0, 50)

    @staticmethod
    def validateLastName(last_name):
        return Validator.validateLength(last_name, 0, 50)
