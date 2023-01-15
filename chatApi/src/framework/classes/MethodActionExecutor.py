from chatApi.src.framework.classes.Action import Action

class MethodActionExecutor:

    def __init__(self):
        self._actions = {}

    def setMethodAction(self, method: str, action: Action):
        self._actions[method] = action

    def executeAction(self, request):
        action = self._actions[request.method]()
        
        body = request.GET if request.method == 'GET' else request.POST
        if hasattr(action, 'setInput') and callable(getattr(action, 'setInput')):
            action.setInput(body)

        if not action.verifyAccess():
            raise Exception("User does not have access")

        if not action.validateInput():
            raise Exception("Invalid input")

        return action.execute()