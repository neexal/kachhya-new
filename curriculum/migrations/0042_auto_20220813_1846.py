# Generated by Django 3.1.4 on 2022-08-13 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0041_auto_20220813_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
