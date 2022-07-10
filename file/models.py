from django.db import models
from datetime import datetime


class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/', null=False, default="")
    description = models.TextField()
    date_uploaded = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
