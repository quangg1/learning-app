from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ShoppingcartDetails(models.Model):
    shopping_cart = models.ForeignKey(
        'Shoppingcart',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    course = models.ForeignKey(
        'Course',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1)],
        blank=False,
        null=False
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
        db_table = 'shoppingcart_details'

    def __str__(self):
        return f'{self.shopping_cart} - {self.course} - {self.quantity}'