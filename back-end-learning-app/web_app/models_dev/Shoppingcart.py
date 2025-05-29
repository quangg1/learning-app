from django.db import models


class Shoppingcart(models.Model):
    user = models.ForeignKey(
        'User',
        models.CASCADE,
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
        db_table = 'shoppingcart'

    def __str__(self):
        return f'{self.user} - {self.created_at}'