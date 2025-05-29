from django.db import models


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(
        'User',
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

    sentiment = models.CharField(
        max_length=255,
        blank=True,
        null=True
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
        db_table = 'comment'

    def __str__(self):
        return f'{self.user} - {self.course} - {self.content}'