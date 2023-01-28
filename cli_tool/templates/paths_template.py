from cli_tool.config import config

def paths_template(module_name: str):

    return f"""from {config["project_name"]}.src.framework.classes.PathBuilder import PathBuilder
from {config["project_name"]}.src.modules.{module_name}.views.ViewFactory import ViewFactory

def ProfilePaths() -> list:
    path_builder = PathBuilder()
    view_factory = ViewFactory()
    
    path_builder.set_path('profile/get/all', view_factory.GetAllProfilesView())
    path_builder.set_path('profile/get/<str:username>', view_factory.GetProfileView())
    path_builder.set_path('profile/create', view_factory.CreateProfileView())

    return path_builder.get_path_list()"""