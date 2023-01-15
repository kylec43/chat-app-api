from chatApi.src.classes.Input import Input

class GetProfileInput(Input):

    def setInputFromBody(self, body):
        self.username = body['username']

    def validate(self):
        return len(self.username) <= 50