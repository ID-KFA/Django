from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from author.models import AuthorsModel


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(0, 5):
            user = AuthorsModel(name=f"Автор_{i}",
                                surname=f"Фамилия_{i}",
                                email=f"author{i}@tyt.ru",
                                bio=lorem_ipsum.words(10),
                                dob="1900-11-12")
            user.save()
        self.stdout.write("Создание авторов выполнено")
