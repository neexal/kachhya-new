# Generated by Django 3.1.4 on 2022-08-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0036_auto_20220813_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]