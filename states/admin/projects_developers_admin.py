from django.contrib import admin
from ..models import ProjectDevelopers


@admin.register(ProjectDevelopers)
class ProjectDevelopersAdmin(admin.ModelAdmin):
    list_display = ("__str__",)