from django.db import models

class LegacyModel(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'legacy_model'
