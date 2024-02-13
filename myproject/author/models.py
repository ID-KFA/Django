from django.db import models
from django.urls import reverse

# Create your models here.
"""
Создайте модель Автор. Модель должна содержать
следующие поля:
○ имя до 100 символов
○ фамилия до 100 символов
○ почта
○ биография
○ день рождения
Дополнительно создай пользовательское поле “полное
имя”, которое возвращает имя и фамилию.


Создайте модель Статья (публикация). Авторы из прошлой задачи могут
писать статьи. У статьи может быть только один автор. У статьи должны быть
следующие обязательные поля:
○ заголовок статьи с максимальной длиной 200 символов
○ содержание статьи
○ дата публикации статьи
○ автор статьи с удалением связанных объектов при удалении автора
○ категория статьи с максимальной длиной 100 символов
○ количество просмотров статьи со значением по умолчанию 0
○ флаг, указывающий, опубликована ли статья со значением по умолчанию
False

Создайте модель Комментарий.
Авторы могут добавлять комментарии к своим и чужим
статьям. Т.е. у комментария может быть один автор.
И комментарий относится к одной статье. У модели должны
быть следующие поля
○ автор
○ статья
○ комментарий
○ дата создания
○ дата изменения



Доработаем задачи из прошлого семинара по созданию моделей автора, статьи и 
комментария.
Создайте шаблон для вывода всех статей автора в виде списка заголовков.
Если статья опубликована, заголовок должен быть ссылкой на статью.
Если не опубликована, без ссылки.
Не забываем про код представления с запросом к базе данных и маршруты.

Доработаем задачу 4.
Создай шаблон для вывода подробной информации о статье.
Внесите изменения в views.py - создайте представление и в urls.py - добавьте 
маршрут.

*Увеличивайте счётчик просмотра статьи на единицу при каждом просмотре


Продолжаем работу с авторами, статьями и комментариями.
Создайте форму для добавления нового автора в базу данных.
Используйте ранее созданную модель Author
"""


class AuthorsModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    dob = models.DateField()
    fullname = models.CharField(blank=True, null=True, max_length=120)

    def save(self, *args, **kwargs):
        self.fullname = self.name + " " + self.surname
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname


class ArticleModel(models.Model):
    author = models.ForeignKey(AuthorsModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pubicated_date = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    publicated_flag = models.BooleanField(default=False)

        # def get_absolute_url(self):
        # return reverse("article_page", kwargs={"article_id": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(AuthorsModel, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    text = models.TextField()
    changed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
