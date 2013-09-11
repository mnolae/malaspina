from django.utils.translation import ugettext_lazy as _

from django.db import models

import datetime

class Event(Page):
    sdata = models.CharField(max_length=10)
    sdate = models.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Event list")