def entity_template(module_name: str):
    return f"""from django.db import models

class {module_name}(models.Model):
    id = models.BigAutoField(primary_key=True)
    column = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = '{module_name.lower()}'

    def __str__(self):
        return f"{{self.id}} {{self.column}}"
    """