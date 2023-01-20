from cli_tool.config import config

def input_template(module_name: str):
    return f"""from {config["project_name"]}.src.framework.classes.InputBase import InputBase

class Get{module_name}Input(InputBase):

    def set_from_body(self, body):
        self.id = body['id']

    def validate(self):
        return id != None
    """