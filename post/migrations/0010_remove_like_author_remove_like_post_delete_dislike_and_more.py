# Generated by Django 5.1.3 on 2024-11-24 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_dislike_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='author',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.DeleteModel(
            name='DisLike',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]