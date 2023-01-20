from cli_tool.config import config

def controller_template(module_name: str):

    return f"""from {config["project_name"]}.src.modules.{module_name}.services.ServiceFactory import ServiceFactory
from {config["project_name"]}.src.modules.{module_name}.input.{module_name}Input import {module_name}Input
from {config["project_name"]}.src.framework.classes.RequestWrapper import RequestWrapper

class {module_name}Controller:

    def __init__(self):
        self.service_factory = ServiceFactory()
        self.{module_name.lower()}_service = self.service_factory.{module_name}Service()

    def get_{module_name.lower()}(self, request: RequestWrapper):
        input = {module_name}Input()
        input.set_from_body(request.get_body())

        if not input.validate():
            raise Exception("Invalid input")

        return self.{module_name.lower()}_service.get_{module_name.lower()}(input.id)
    """