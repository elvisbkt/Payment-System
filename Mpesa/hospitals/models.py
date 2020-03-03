from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255, null=False)
    location = models.Charfield(max_length=255, null=False)
    tillNumber = models.IntegerField()

    def __str__(self):
        return self.name