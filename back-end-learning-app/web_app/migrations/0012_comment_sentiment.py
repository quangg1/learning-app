# Generated by Django 5.0.6 on 2024-05-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0011_alter_submission_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='sentiment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
