# Generated by Django 3.1 on 2022-08-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_id',
            field=models.IntegerField(max_length=100, unique=True),
        ),
    ]