# Generated by Django 4.0.1 on 2022-09-09 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0052_lesson_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='counter',
        ),
    ]