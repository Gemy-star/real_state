from django.db import models
from django.utils.translation import gettext_lazy as _
from ..models import Department


class State(models.Model):
    STATE_TYPE = (
        (1, 'فيلا'),
        (2, 'شقة'),
        (3, 'دوبلكس'),
    )
    status = models.CharField(_("status of state"), max_length=50)
    date_received = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    state_type = models.SmallIntegerField(null=True, blank=True, choices=STATE_TYPE)
    area = models.IntegerField(null=True, blank=True)
    max_price = models.SmallIntegerField(null=True, blank=True)
    min_price = models.SmallIntegerField(null=True, blank=True)
    rooms_number = models.SmallIntegerField(null=True, blank=True)
    bathroom_number = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        pass
