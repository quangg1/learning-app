from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator


class Crypto(models.Model):
    currency_usd = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=False,
        blank=False,
        db_index=True
    )
    suply = models.DecimalField(
        max_digits=30,
        decimal_places=20,
        validators=[MinValueValidator(0)],
        null=False,
        blank=False
    )
    amount_buy = models.DecimalField(
        max_digits=30,
        decimal_places=20,
        validators=[MinValueValidator(0)],
        null=False,
        blank=False
    )
    amount_sell = models.DecimalField(
        max_digits=30,
        decimal_places=20,
        validators=[MinValueValidator(0)],
        null=False,
        blank=False
    )
    crypto_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        db_index=True
    )
    url_img = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    author = models.ForeignKey(
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
        db_table = 'crypto'

    def __str__(self):
        return f'{self.crypto_name} - {self.amount_buy} - {self.amount_sell}'
    
    def save(self, *args, **kwargs):
        super(Crypto, self).save(*args, **kwargs)