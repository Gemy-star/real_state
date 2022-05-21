from django.db import models
from ..models import (
    Country
)
from django.templatetags.static import static


class Department(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, help_text='Department Name')
    description = models.TextField(null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)
    background = models.ImageField(upload_to='department-backgrounds/', null=True, blank=True)

    @property
    def background_url(self):
        if self.background and hasattr(self.background, 'url'):
            return self.background.url
        else:
            return static("assets/img/gallery/cinnamon.png")

    def __str__(self) -> str:
        return f"Name: {self.name}"
