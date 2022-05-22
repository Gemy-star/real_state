from django.db import models
from ..models import Department
from django.templatetags.static import static


class Projects(models.Model):
    project_name = models.CharField(max_length=255, null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    min_price = models.SmallIntegerField(null=True, blank=True)
    max_price = models.SmallIntegerField(null=True, blank=True)
    department = models.ForeignKey(Department, null=True, blank=True, related_name='projects', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='projects-photos/', null=True, blank=True)
    background_1 = models.ImageField(upload_to='projects-photos/', null=True, blank=True)
    background_2 = models.ImageField(upload_to='projects-photos/', null=True, blank=True)
    background_3 = models.ImageField(upload_to='projects-photos/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    @property
    def cover_url(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url
        else:
            return static("assets/img/gallery/cinnamon.png")

    @property
    def background_1_url(self):
        if self.background_1 and hasattr(self.background_1, 'url'):
            return self.background_1.url
        else:
            return static("assets/img/gallery/cinnamon.png")

    @property
    def background_2_url(self):
        if self.background_1 and hasattr(self.background_2, 'url'):
            return self.background_2.url
        else:
            return static("assets/img/gallery/cinnamon.png")

    @property
    def background_3_url(self):
        if self.background_1 and hasattr(self.background_3, 'url'):
            return self.background_3.url
        else:
            return static("assets/img/gallery/cinnamon.png")

    def __str__(self) -> str:
        return f"Name : {self.project_name}"

    @property
    def CheckEvenPK(self):
        return True if (self.pk % 2) == 0 else False
