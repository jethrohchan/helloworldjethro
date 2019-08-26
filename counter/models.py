from django.db import models
from django.conf import settings

class Counter(models.Model):
    visits = models.IntegerField(null=False, default=0)

    def __str__(self):
        return 'Count'
