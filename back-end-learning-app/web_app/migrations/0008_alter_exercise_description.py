# Generated by Django 5.0.6 on 2024-05-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0007_exercise_tagname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.TextField(max_length=3000),
        ),
    ]
