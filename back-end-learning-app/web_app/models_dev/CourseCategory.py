from django.db import models



class CourseCategory(models.Model):
    course = models.ForeignKey(
        'Course',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    category = models.ForeignKey(
        'Category',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=False,
        null=False,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'course_category'

    def __str__(self):
        return f'{self.course} - {self.category}'
    
    def save(self, *args, **kwargs):
        super(CourseCategory, self).save(*args, **kwargs)