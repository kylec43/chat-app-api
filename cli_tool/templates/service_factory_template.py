from cli_tool.config import config

def service_factory_template(module_name: str):
    return f"""from {config["project_name"]}.src.modules.{module_name}.services.{module_name}Service import {module_name}Service

class ServiceFactory:

    def {module_name}Service(self):
        return {module_name}Service()
    """