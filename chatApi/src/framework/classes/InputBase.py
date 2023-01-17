import abc

class InputBase:

    @abc.abstractmethod
    def set_from_body(body):
        pass

    @abc.abstractmethod
    def validate():
        pass