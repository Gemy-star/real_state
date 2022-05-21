from django.db import models
from ..models import (
    State,
    Developers
)


class StateDeveloper(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developers, on_delete=models.CASCADE)

    class Meta:
        pass
