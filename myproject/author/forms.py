"""
Продолжаем работу с авторами, статьями и комментариями.
Создайте форму для добавления нового автора в базу данных.
Используйте ранее созданную модель Author

Аналогично автору создайте форму добавления новой статьи.
Автор статьи должен выбираться из списка (все доступные в базе данных авторы).
"""

from django import forms
from .models import AuthorsModel, ArticleModel


class Game(forms.Form):
    choose = forms.ChoiceField(choices=[("coin", "Монетка"), ("dice", "Кости"),
                                        ("rand_number", "Случайное число")])
    attempts = forms.IntegerField(min_value=1, max_value=64)


class NewAuthor(forms.ModelForm):
    # name = models.CharField(max_length=100)
    # surname = models.CharField(max_length=100)
    # email = models.EmailField()
    # bio = models.TextField()
    # dob = models.DateField()
    # fullname = models.CharField(blank=True, null=True, max_length=120)
    class Meta:
        model = AuthorsModel
        fields = ["name", "surname", "email", "bio", "dob"]

class NewArticle(forms.ModelForm):
    # author = models.ForeignKey(AuthorsModel, on_delete=models.CASCADE)
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    # pubicated_date = models.DateTimeField(auto_now_add=True)
    #
    # category = models.CharField(max_length=100)
    # views_count = models.IntegerField(default=0)
    # publicated_flag = models.BooleanField(default=False)

    class Meta:
        model = ArticleModel
        fields = ["author","title", "text", "category", "publicated_flag"]