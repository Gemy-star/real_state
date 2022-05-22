from django.contrib import admin
from ..models import StateDeveloper


@admin.register(StateDeveloper)
class StateDeveloperAdmin(admin.ModelAdmin):
    list_display = ("__str__",)