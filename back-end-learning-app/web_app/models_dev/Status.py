from django.db import models


class Status(models.Model):
    status_name = models.CharField(
        max_length=255,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'status'

    def __str__(self):
        return self.status_name