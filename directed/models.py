from django.db import models

class RenamedDirectedModel(models.Model):
    name = models.CharField(max_length=10)
    legacy = models.ForeignKey("legacy.LegacyModel", on_delete=models.CASCADE)
