from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import ForeignKey
from django.shortcuts import render
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    author = ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    category = ForeignKey('Category', on_delete=models.CASCADE)
    com_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Категория", null=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Comments(models.Model):
    text = models.TextField(blank=True, verbose_name="Комментарий")
    post = ForeignKey(Posts, on_delete=models.CASCADE, null=True)
    author = ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
