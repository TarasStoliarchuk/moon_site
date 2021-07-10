from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    login_time = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14, verbose_name='Номер')
    avatar = models.ImageField(upload_to='avatar/', verbose_name='Аватар', blank=True, null=True)
    bio = models.TextField(blank=True, null=True, verbose_name='О себе')
    birthday = models.DateField(blank=True, null=True, verbose_name='День рождения')
    gender = models.CharField(max_length=6, choices=GENDER, default='Пол')


class Post(models.Model):
    author = models.ForeignKey(Profile, related_name='post', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', verbose_name='Фото')
    text = models.TextField(verbose_name='Текст под  постом')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    author = models.ForeignKey(Profile, related_name='coment', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')
