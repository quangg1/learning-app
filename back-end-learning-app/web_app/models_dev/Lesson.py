from django.db import models

class Lesson(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        db_index=True
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    course = models.ForeignKey(
        'Course',
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
        db_table = 'lesson'

    def __str__(self):
        return f'{self.title}'