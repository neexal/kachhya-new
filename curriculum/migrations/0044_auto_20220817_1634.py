# Generated by Django 3.1.4 on 2022-08-17 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0043_auto_20220813_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='marks',
        ),
        migrations.AddField(
            model_name='assignment',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='curriculum.lesson'),
        ),
    ]
