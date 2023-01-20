import os
from cli_tool.config import config
from templates.entity_template import entity_template
from templates.controller_template import controller_template
from templates.input_template import input_template
from templates.input_serializer_template import input_serializer_template
from templates.routes_template import routes_template
from templates.service_template import service_template
from templates.service_factory_template import service_factory_template

def create_module(module_name: str):
    module_name = module_name.title()

    if not os.path.isdir(f"../{config['project_name']}/src/modules"):
        os.mkdir(f"../{config['project_name']}/src/modules")

    if os.path.isdir(f"../{config['project_name']}/src/modules/{module_name}"):
        print("Module already exists")
        return
    else:
        os.mkdir(f"../{config['project_name']}/src/modules/{module_name}")

    os.mkdir(f"../{config['project_name']}/src/modules/{module_name}/entities")
    with open(f"../{config['project_name']}/src/modules/{module_name}/entities/{module_name}.py", 'w') as entityFile:
        entityFile.write(input_serializer_template(module_name))

    with open(f"../{config['project_name']}/src/modules/{module_name}/entities/{module_name}Serializer.py", 'w') as entityFile:
        entityFile.write(entity_template(module_name))

    with open(f"../{config['project_name']}/src/modules/{module_name}/{module_name}Controller.py", 'w') as entityFile:
        entityFile.write(controller_template(module_name))

    os.mkdir(f"../{config['project_name']}/src/modules/{module_name}/input")
    with open(f"../{config['project_name']}/src/modules/{module_name}/input/{module_name}Input.py", 'w') as entityFile:
        entityFile.write(input_template(module_name))

    with open(f"../{config['project_name']}/src/modules/{module_name}/{module_name}Routes.py", 'w') as entityFile:
        entityFile.write(routes_template(module_name))

    os.mkdir(f"../{config['project_name']}/src/modules/{module_name}/services")
    with open(f"../{config['project_name']}/src/modules/{module_name}/services/{module_name}Service.py", 'w') as entityFile:
        entityFile.write(service_template(module_name))

    with open(f"../{config['project_name']}/src/modules/{module_name}/services/ServiceFactory.py", 'w') as entityFile:
        entityFile.write(service_factory_template(module_name))

    