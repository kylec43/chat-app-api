from chatApi.src.framework.classes.RequestWrapper import RequestWrapper

class MethodActionExecutor:

    def __init__(self):
        self._actions = {}

    def setMethodAction(self, method: str, action: callable):
        self._actions[method] = action

    def executeAction(self, request):
        requestWrapper = RequestWrapper(request)
        action = self._actions[requestWrapper.get_method()]
        return action(requestWrapper)