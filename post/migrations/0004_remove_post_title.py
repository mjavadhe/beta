# Generated by Django 5.0.7 on 2024-08-28 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]