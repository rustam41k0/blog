# Generated by Django 4.0.5 on 2022-06-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_remove_posts_comments_comments_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='com_count',
            field=models.CharField(max_length=255, null=True),
        ),
    ]