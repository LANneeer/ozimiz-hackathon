from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True
