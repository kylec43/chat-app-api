class Validator:
    
    @staticmethod
    def validateLength(value, min=0, max=None):
        return len(value) >= min and True if max == None else len(value) <= max