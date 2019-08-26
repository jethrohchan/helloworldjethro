from django.db import models
from django.conf import settings

class Counter(models.Model):
    count = models.IntegerField(null=True)

    def __str__(self):
        return self.title
