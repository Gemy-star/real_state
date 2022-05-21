from django.db import models


class Projects(models.Model):
    project_name = models.CharField(max_length=255, null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)
    area = models.SmallIntegerField(null=True, blank=True)
    min_price = models.SmallIntegerField(null=True, blank=True)
    max_price = models.SmallIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Name : {self.project_name}"

    @property
    def carsoualNbr(self):
        return self.pk * 100
