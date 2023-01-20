class Validator:
    
    @staticmethod
    def validateLength(value, min=0, max=None):
        return len(value) >= min and True if max == None else len(value) <= max

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