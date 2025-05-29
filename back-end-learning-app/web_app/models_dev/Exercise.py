from django.db import models


class Exercise(models.Model):
    tagname = models.ManyToManyField(
        'Tagname',
        blank=True,
        null=True,
        db_index=True,
        related_name='exercises'
    )
    title = models.CharField(
        max_length=255,
        db_index=True
    )
    description = models.TextField(
        blank=False,
        null=False,
        max_length=3000
    )
    detail_lesson = models.ForeignKey(
        'Detaillesson',
        models.CASCADE,
        blank=True,
        null=True,
        db_index=True
    )
    link_solution = models.TextField(
        blank=True,
        null=True,
        max_length=1000,
        db_index=True
    )
    code_solution = models.TextField(
        blank=True,
        null=True,
        max_length=1000,
        db_index=True
    )
    extent = models.ForeignKey(
        'Extent',
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
        db_table = 'exercise'

    def __str__(self):
        return f'{self.title} - {self.extent}'
    
    def get_all_tagname(self):
        return ', '.join([tagname.name for tagname in self.tagname.all()]) if self.tagname.all() else []