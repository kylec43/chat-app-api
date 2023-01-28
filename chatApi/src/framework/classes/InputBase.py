import abc

class InputBase:

    @abc.abstractmethod
    def set(self, data: dict):
        pass

    @abc.abstractmethod
    def validate(self):
        pass

    def serialize(self):
        return self.__dict__