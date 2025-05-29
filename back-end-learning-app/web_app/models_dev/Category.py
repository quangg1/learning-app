from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length=255,
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
        db_table = 'category'

    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        self.category_name = self.category_name.title()
        super(Category, self).save(*args, **kwargs)