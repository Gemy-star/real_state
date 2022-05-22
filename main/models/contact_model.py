from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
