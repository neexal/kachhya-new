# Generated by Django 4.0.1 on 2022-09-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0053_remove_lesson_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='views',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_views', to='curriculum.IpModel'),
        ),
    ]
