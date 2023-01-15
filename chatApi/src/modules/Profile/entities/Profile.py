from django.db import models

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return f"{self.id} {self.username} {self.password} {self.first_name} {self.last_name}"