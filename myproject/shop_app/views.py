from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Order, Client
from django.utils import timezone
from datetime import timedelta



def all_orders(request: HttpRequest, customer_id):
    orders = Order.objects.filter(customer_id=customer_id)

    return render(request, "shop_app/orders.html", {"orders": orders})


def client_orders(request, client_id):
    client = Client.objects.get(id=client_id)

    # Фильтрация заказов по временному интервалу
    week_ago = timezone.now() - timedelta(days=7)
    month_ago = timezone.now() - timedelta(days=30)
    year_ago = timezone.now() - timedelta(days=365)

    week_orders = client.order_set.filter(date_ordered__gte=week_ago)
    month_orders = client.order_set.filter(date_ordered__gte=month_ago)
    year_orders = client.order_set.filter(date_ordered__gte=year_ago)

    # Получение списка товаров без повторений
    week_products = set()
    month_products = set()
    year_products = set()

    for order in week_orders:
        week_products.update(order.products.all())

    for order in month_orders:
        month_products.update(order.products.all())

    for order in year_orders:
        year_products.update(order.products.all())

    context = {
        'client': client,
        'week_products': week_products,
        'month_products': month_products,
        'year_products': year_products
    }

    return render(request, 'shop_app/client.html', context)


