from django.db import models
from ..models import (
    Developers ,
    Projects
)

class ProjectDevelopers(models.Model):
    project = models.ForeignKey(Projects , on_delete=models.CASCADE)
    developer = models.ForeignKey(Developers , on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"project : {self.project.project_name} developer: {self.developer.name}"
