from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    cooking_steps = models.TextField(verbose_name='Как приготовить')
    cooking_time = models.PositiveSmallIntegerField(default=0, verbose_name='Время приготовления')
    image = models.ImageField(upload_to='images/', default='default_image.png', blank=True, verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    ingredients = models.TextField(verbose_name='Ингридиенты', default='')

    class Meta:
        db_table = 'recipe'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_birth = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.user.username