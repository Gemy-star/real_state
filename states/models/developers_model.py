from django.db import models
from django.templatetags.static import static


class Developers(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, help_text='Department Name')
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='developers-icons/', null=True, blank=True)

    @property
    def background_url(self):
        if self.icon and hasattr(self.icon, 'url'):
            return self.icon.url
        else:
            return static("assets/img/gallery/cinnamon.png")

    def __str__(self) -> str:
        return self.name
