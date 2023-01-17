from django.urls import path
from chatApi.src.framework.classes.MethodActionExecutor import MethodActionExecutor

class Router:
    
    def __init__(self):
        self._routes = []
        self._method_action_executors = {}

    def __setEndpointMethodAction__(self, endpoint: str, method: str, action: callable):
        method_action_executor = MethodActionExecutor()

        # set the method action for existing or new endpoint
        if endpoint in self._method_action_executors:
            method_action_executor = self._method_action_executors[endpoint]
        else:
            self._method_action_executors[endpoint] = method_action_executor

        method_action_executor.setMethodAction(method, action)


    def get(self, endpoint: str, action: callable):
        self.__setEndpointMethodAction__(endpoint, 'GET', action)


    def post(self, endpoint: str, action: callable):
        self.__setEndpointMethodAction__(endpoint, 'POST', action)

    
    def __buildRoutes__(self):
        routes = []
        for endpoint, executor in self._method_action_executors.items():
            route = path(endpoint, executor.executeAction)
            routes.append(route)
        
        return routes


    def getRoutes(self):
        self._routes = self.__buildRoutes__()
        return self._routes

    

