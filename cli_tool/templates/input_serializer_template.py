from cli_tool.config import config

def input_serializer_template(module_name: str):

    return f"""from rest_framework import serializers
from {config["project_name"]}.src.modules.{module_name}.entities.{module_name} import {module_name}

class {module_name}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {module_name}
        fields = ['id', 'username', 'password', 'first_name', 'last_name']
    """