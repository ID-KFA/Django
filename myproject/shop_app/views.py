from django.http import HttpRequest
from .models import Order, Client, Product
from django.utils import timezone
from datetime import timedelta
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, HttpResponse
from .models import Product
from .forms import ImageForm, NewProduct


def all_orders(request: HttpRequest, customer_id):
    orders = Order.objects.filter(customer_id=customer_id)

    return render(request, "shop_app/orders.html", {"orders": orders})

def all_products(request):
    # получаем все значения модели
    products = Product.objects.all()
    return render(request, 'shop_app/home_page.html', {'products': products})

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


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'shop_app/upload_image.html', {'form': form})

def index(request):
    products_list = Product.objects.all()
    context_dict = {'products': products_list}
    return render(request, 'index.html', context_dict)


def newproduct(request):
    if request.method == "POST":
        form = NewProduct(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            price = form.cleaned_data["price"]
            amount = form.cleaned_data["amount"]
            product_image = form.cleaned_data['product_image']
            product = Product(title=title, description=description,
                              price=price,
                              amount=amount, product_image=product_image)
            product.save()
        else:
            return render(request, "shop_app/newproduct.html", {"form": form})
    return render(request, "shop_app/newproduct.html", {"form": NewProduct()})

