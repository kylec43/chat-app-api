from chatApi.src.classes.Input import Input

class CreateProfileInput(Input):

    def setInputFromBody(self, body):
        self.username = body['username']
        self.password = body['password']
        self.first_name = body['first_name']
        self.last_name = body['last_name']

    def validate(self):
        return self.__validateLength__(self.username, 50) and self.__validateLength__(self.password, 50) and self.__validateLength__(self.first_name, 50) and self.__validateLength__(self.last_name, 50)

    def __validateLength__(self, input, length):
        return len(input) <= length