from django.db import models
import datetime


class message(models.Model):
    """
    Here you add your table attribute
    """
    msg_text = models.CharField(max_length=1000, blank=True, null=True)
    date_time=models.DateTimeField(default=datetime.datetime.now)
