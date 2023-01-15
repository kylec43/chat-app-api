import abc
import json

class Action(abc.ABC):

    def __init__(self):
        super().__init__()
        self.input = None

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def verifyAccess(self):
        pass

    @abc.abstractmethod
    def validateInput(self):
        pass