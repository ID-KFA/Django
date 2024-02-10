from django.db import models

"""
Создайте три модели Django: клиент, товар и заказ. Клиент
может иметь несколько заказов. Заказ может содержать
несколько товаров. Товар может входить в несколько
заказов.
Поля модели "Клиент":
○ имя клиента
○ электронная почта клиента
○ номер телефона клиента
○ адрес клиента
○ дата регистрации клиента

Поля модели "Товар":
○ название товара
○ описание товара
○ цена товара
○ количество товара
○ дата добавления товара

Поля модели "Заказ":
○ связь с моделью "Клиент", указывает на клиента,
сделавшего заказ
○ связь с моделью "Товар", указывает на товары,
входящие в заказ
○ общая сумма заказа
○ дата оформления заказа
*Допишите несколько функций CRUD для работы с
моделями по желанию. Что по вашему мнению актуально в
такой базе данных.

Доработать магазин
Создайте шаблон для вывода всех заказов клиента и списком товаров внутри 
каждого заказа.
Подготовьте необходимый маршрут и представление.

Домашнее задание задание
Продолжаем работать с товарами и заказами.

Создайте шаблон, который выводит список заказанных клиентом товаров из всех 
его заказов с сортировкой по времени:
— за последние 7 дней (неделю)
— за последние 30 дней (месяц)
— за последние 365 дней (год)

Товары в списке не должны повторятся.


"""


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(default=0)
    product_added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} купил товаров на сумму {self.total_price}"
