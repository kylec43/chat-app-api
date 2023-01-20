from django.urls import path

class PathContainer:

    def __init__(self):
        self.paths = []

    def add(self, *routesList: callable):
        for routes in routesList:
            self.paths.extend(routes())

        return self

    def getPaths(self):
        return self.paths