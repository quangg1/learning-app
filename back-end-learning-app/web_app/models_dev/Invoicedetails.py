from django.db import models



class Invoicedetails(models.Model):
    invoice = models.ForeignKey(
        'Invoice',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    shopping_cart_details = models.ForeignKey(
        'ShoppingcartDetails',
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
        db_table = 'invoicedetails'

    def __str__(self):
        return f'{self.invoice} - {self.shopping_cart_details}'