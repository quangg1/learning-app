from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Extent(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
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
        db_table = 'extent'

    def __str__(self):
        return f'{self.name}'
