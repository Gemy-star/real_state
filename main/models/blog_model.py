from django.db import models
from django.templatetags.static import static
from states.models import Projects


class Blog(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    mini_description = models.TextField(null=True, blank=True)
    full_description = models.TextField(null=True, blank=True)
    more_description = models.TextField(null=True, blank=True)
    background = models.ImageField(upload_to='blogs-images/', null=True, blank=True)
    project = models.ForeignKey(Projects, null=True, blank=True, on_delete=models.CASCADE)

    @property
    def background_url(self):
        if self.background and hasattr(self.background, 'url'):
            return self.background.url
        else:
            return static("assets/img/gallery/cinnamon.png")
