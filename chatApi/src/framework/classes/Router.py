from django.urls import path
from chatApi.src.framework.classes.Action import Action
from chatApi.src.framework.classes.MethodActionExecutor import MethodActionExecutor

class Router:
    
    def __init__(self):
        self._routes = []
        self._methodActionExecutors = {}

    def __setEndpointMethodAction__(self, endpoint: str, method: str, action: Action):
        action_executor = MethodActionExecutor()
        if endpoint in self._methodActionExecutors:
            action_executor = self._methodActionExecutors[endpoint]
        else:
            self._methodActionExecutors[endpoint] = action_executor

        action_executor.setMethodAction(method, action)


    def get(self, endpoint: str, action: Action):
        self.__setEndpointMethodAction__(endpoint, 'GET', action)


    def post(self, endpoint: str, action: Action):
        self.__setEndpointMethodAction__(endpoint, 'POST', action)

    
    def __buildRoutes__(self):
        for endpoint, executor in self._methodActionExecutors.items():
            route = path(endpoint, executor.executeAction)
            self._routes.append(route)


    def getRoutes(self):
        self.__buildRoutes__()
        return self._routes

    

