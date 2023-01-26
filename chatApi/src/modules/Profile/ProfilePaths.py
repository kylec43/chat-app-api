from chatApi.src.framework.classes.PathBuilder import PathBuilder
from chatApi.src.modules.Profile.views.ViewFactory import ViewFactory

def ProfilePaths() -> list:
    path_builder = PathBuilder()
    view_factory = ViewFactory()
    
    path_builder.set_path('profile/get/all', view_factory.GetAllProfilesView())
    path_builder.set_path('profile/get/<str:username>', view_factory.GetProfileView())
    path_builder.set_path('profile/create', view_factory.CreateProfileView())

    return path_builder.get_path_list()
