# Generated by Django 4.0.1 on 2022-09-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0048_auto_20220818_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='id',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_id',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
