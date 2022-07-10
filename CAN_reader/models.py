from django.db import models
from file.models import Document


class Parser(models.Model):
    name = models.CharField(max_length=100)
    place1 = models.CharField(max_length=100)
    place2 = models.CharField(max_length=100)
    place3 = models.CharField(max_length=100)
    place4 = models.CharField(max_length=100)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
