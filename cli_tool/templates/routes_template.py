from cli_tool.config import config

def routes_template(module_name: str):

    return f"""from {config["project_name"]}.src.framework.classes.Router import Router
from {config["project_name"]}.src.modules.{module_name}.{module_name}Controller import {module_name}Controller

def {module_name}Routes():
    router = Router()
    {module_name.lower()}_controller = {module_name}Controller()
    
    router.get('{module_name.lower()}', {module_name.lower()}_controller.get_{module_name.lower()})

    return router.getRoutes()
    """