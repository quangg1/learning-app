from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator



class Course(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        db_index=True
    )
    description = models.TextField( #* No has min_length, default >= 1
        blank=False,
        null=False,
        max_length=1000,
    )
    price = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(1000000)],
        db_index=True
    )
    instructor = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=True,
        null=True,
        db_index=True
    )
    discount = models.ForeignKey(
        'Discount',
        models.SET_NULL,
        blank=True,
        null=True,
        db_index=True
    )
    extent = models.ForeignKey(
        'Extent',
        models.SET_NULL,
        blank=False,
        null=True,
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
        db_table = 'course'

    def __str__(self):
        return f'{self.title} - {self.price} - {self.instructor}'
    
    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)