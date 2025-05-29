from django.db import models
from django.utils.text import slugify


class Tagname(models.Model):
    slug_tagname = models.SlugField(max_length=255, blank=True, null=True, db_index=True, unique=True, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True, db_index=True)

    class Meta:
        db_table = 'tagname'

    def __str__(self):
        return f'''Slug: {self.slug_tagname} - Tên: {self.name}'''
    
    def save(self, *args, **kwargs):
        self.slug_tagname = slugify(self.name)
        super(Tagname, self).save(*args, **kwargs)