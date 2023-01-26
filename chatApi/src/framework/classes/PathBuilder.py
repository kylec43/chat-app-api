from django.urls import path
from rest_framework.generics import CreateAPIView

class PathBuilder:
    
    def __init__(self):
        self._path_views = {}

    def set_path(self, path: str, view: CreateAPIView):
        self._path_views[path] = view
    
    def __build_paths__(self) -> list:
        return [path(endpoint, view.as_view()) for endpoint, view in self._path_views.items()]

    def get_path_list(self) -> list:
        return self.__build_paths__()
    

