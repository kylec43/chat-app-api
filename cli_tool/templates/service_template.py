from cli_tool.config import config

def service_template(module_name: str):

    return f"""from {config["project_name"]}.src.modules.{module_name}.entities.{module_name} import {module_name}
from {config["project_name"]}.src.modules.{module_name}.entities.{module_name}Serializer import {module_name}Serializer
from django.http import JsonResponse

class {module_name}Service:
    def get_{module_name.lower()}(self, id):
        user = {module_name}.objects.get(id=id)
        serializer = {module_name}Serializer(user)
        return JsonResponse(serializer.data, safe=False)
    """