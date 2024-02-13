from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from author.models import AuthorsModel, ArticleModel
from random import choice


class Command(BaseCommand):
    def handle(self, *args, **options):
        authors = AuthorsModel.objects.all()
        for i in range(0, 5):
            article = ArticleModel(
                author=choice(authors),
                title=f"Статья № {i}",
                text=lorem_ipsum.paragraphs(4),
                category=f"Категория {i}",
                pubicated_flag=choice([True, False])
            )
            article.save()
        self.stdout.write("Создание публикаций выполнено")
