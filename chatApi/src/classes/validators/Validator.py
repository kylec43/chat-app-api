class Validator:
    
    @staticmethod
    def validate_length(value, min=0, max=None):
        return len(value) >= min and True if max == None else len(value) <= max

    @staticmethod
    def validate_username(username):
        return Validator.validate_length(username, 0, 50)

    @staticmethod
    def validate_password(password):
        return Validator.validate_length(str(password), 0, 50)

    @staticmethod
    def validate_first_name(first_name):
        return Validator.validate_length(first_name, 0, 50)

    @staticmethod
    def validate_last_name(last_name):
        return Validator.validate_length(last_name, 0, 50)