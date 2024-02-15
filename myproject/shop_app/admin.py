from django.contrib import admin

from .models import Client, Product, Order


# Register your models here.
# admin.site.register(Client)
# admin.site.register(Product)
admin.site.register(Order)




@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address"]
    readonly_fields = ["registration_date"]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Контактные данные',
                'fields': ["email", 'phone', "address"],
            },
        ),
        (

            'Дата регистрации',
            {
                'fields': ['registration_date'],
            },
        ),
    ]


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ["title", "description", "price", "amount", "product_image"]
    readonly_fields = ["product_added_date"]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Описание товара',
            {
                'classes': ['collapse'],
                'description': 'Подробности',
                'fields': ["description", "price", "amount", "product_image"]
            },
        ),
        (

            'Прочее',
            {
                'description': 'Дата добавления в базу',
                'fields': ["product_added_date"]
            },
        ),

    ]


# @admin.register(Order)
# class Order(admin.ModelAdmin):
#     list_display = ["customer", "products", "total_price"]
#     filter_horizontal = ["customer"]
#     readonly_fields = ["date_ordered"]
#
#     fieldsets = [
#         (
#             None,
#             {
#                 'classes': ['wide'],
#                 'fields': ["customer"],
#
#             },
#         ),
#         (
#             'Детали заказа',
#             {
#                 'classes': ['collapse'],
#                 'fields': ["products", "total_price"]
#
#             },
#         ),
#         (
#
#             'Прочее',
#             {
#                 'description': 'Дата покупки',
#                 'fields': ["date_ordered"]
#             },
#         ),
#
#     ]
