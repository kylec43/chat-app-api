import abc

class Input:

    @abc.abstractmethod
    def setInputFromBody(body):
        pass

    @abc.abstractmethod
    def validate():
        pass