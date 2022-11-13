# Generated by Django 4.0.5 on 2022-06-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_alter_posts_com_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='com_count',
            field=models.IntegerField(default=0),
        ),
    ]
