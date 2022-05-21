from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, help_text='Country Name')
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Name: {self.name}"
