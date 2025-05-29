from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator


class User(AbstractUser):
    username = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        db_index=True
    )
    email = models.EmailField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        db_index=True,
        validators=[EmailValidator()]
    )

    full_name = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    phone = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    password = models.CharField(
        max_length=255,
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
        db_table = 'auth_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = f"{self.first_name} {self.last_name}".strip()
        super().save(*args, **kwargs)
