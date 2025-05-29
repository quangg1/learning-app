from django.db import models
from django.core.validators import MinValueValidator




class Invoice(models.Model):
    user = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    total_price = models.DecimalField(
        validators=[MinValueValidator(0)],
        max_digits=30,
        decimal_places=2,
        blank=False,
        null=False,
        db_index=True
    )
    status = models.ForeignKey(
        'Status',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        db_index=True
    )

    class Meta:
        db_table = 'invoice'

    def __str__(self):
        return f'{self.user} - {self.total_price} - {self.status}'