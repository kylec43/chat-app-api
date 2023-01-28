import os
from cli_tool.config import config
from templates.entity_template import entity_profile_template, entity_serializer_profile_template, entity_serializer_auth_user_template
from templates.view_template import view_factory_template, view_create_profile_template, view_get_all_profiles_template, view_get_profile_template
from templates.input_template import input_get_profile_template, input_create_profile_template
from templates.paths_template import paths_template
from templates.service_template import service_template, service_factory_template

def create_module(module_name: str):
    module_name = module_name.title()

    # Create Module folder if it doesn't exist
    if not os.path.isdir(f"../{config['project_name']}/src/modules"):
        os.mkdir(f"../{config['project_name']}/src/modules")

    if os.path.isdir(f"../{config['project_name']}/src/modules/{module_name}"):
        print("Module already exists")
        return
    else:
        os.mkdir(f"../{config['project_name']}/src/modules/{module_name}")


    # Create Entities
    # os.mkdir(f"../{config['project_name']}/src/entities")
    # os.mkdir(f"../{config['project_name']}/src/entities/base")
    # os.mkdir(f"../{config['project_name']}/src/entities/serializers")
    # with open(f"../{config['project_name']}/src/modules/{module_name}/entities/AuthUserSerializer.py", 'w') as entityFile:
    #     entityFile.write(entity_serializer_auth_user_template())

    # with open(f"../{config['project_name']}/src/modules/{module_name}/entities/Profile.py", 'w') as entityFile:
    #     entityFile.write(entity_serializer_profile_template(module_name))

    # with open(f"../{config['project_name']}/src/modules/{module_name}/entities/ProfileSerializer.py", 'w') as entityFile:
    #     entityFile.write(entity_profile_template())


    # Create Views
    os.mkdir(f"../{config['project_name']}/src/modules/{module_name}/views")
    with open(f"../{config['project_name']}/src/modules/{module_name}/views/CreateProfileView.py", 'w') as entityFile:
        entityFile.write(view_create_profile_template(module_name))

    with open(f"../{config['project_name']}/src/modules/{module_name}/views/GetProfileView.py", 'w') as entityFile:
        entityFile.write(view_get_profile_template(module_name))

    with open(f"../{config['project_name']}/src/modules/{module_name}/views/GetAllProfilesView.py", 'w') as entityFile:
        entityFile.write(view_get_all_profiles_template(module_name))

    with open(f"../{config['project_name']}/src/modules/{module_name}/views/ViewFactory.py", 'w') as entityFile:
        entityFile.write(view_factory_template(module_name))


    # Create Inputs
    os.mkdir(f"../{config['project_name']}/src/modules/{module_name}/input")
    with open(f"../{config['project_name']}/src/modules/{module_name}/input/CreateProfileInput.py", 'w') as entityFile:
        entityFile.write(input_create_profile_template())

    with open(f"../{config['project_name']}/src/modules/{module_name}/input/GetProfileInput.py", 'w') as entityFile:
        entityFile.write(input_get_profile_template())

    # Create Paths
    with open(f"../{config['project_name']}/src/modules/{module_name}/ProfilePaths.py", 'w') as entityFile:
        entityFile.write(paths_template(module_name))

    # Create Service
    os.mkdir(f"../{config['project_name']}/src/modules/{module_name}/services")
    with open(f"../{config['project_name']}/src/modules/{module_name}/services/ProfileService.py", 'w') as entityFile:
        entityFile.write(service_template(module_name))

    with open(f"../{config['project_name']}/src/modules/{module_name}/services/ServiceFactory.py", 'w') as entityFile:
        entityFile.write(service_factory_template(module_name))

    