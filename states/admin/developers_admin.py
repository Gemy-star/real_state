from django.contrib import admin
from ..models import Developers


@admin.register(Developers)
class DevelopersAdmin(admin.ModelAdmin):
    list_display = ("__str__",)