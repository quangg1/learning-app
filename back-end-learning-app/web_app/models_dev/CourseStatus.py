from django.db import models


class CourseStatus(models.Model):
    course = models.ForeignKey(
        'Course',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    status = models.ForeignKey(
        'Status',
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
        db_table = 'course_status'
        unique_together = ('course', 'status')

    def __str__(self):
        return f'{self.course} - {self.status}'