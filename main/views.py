from django.http import JsonResponse
from django.shortcuts import render
from .models import Item, Order, Discount, Tax
import stripe


def index(request):
    return render(request, 'main/default.html')


def cancel(request):
    return render(request, 'main/cancel.html')


def success(request):
    return render(request, 'main/success.html')


def buy(request, pk):
    stripe.api_key = 'sk_test_51MaQIsCGccPEKImWzia2XABWZFG7q2vIgHFlSK8KftR9ToxfLOv9ZwrIiqatvsSZoRaTKcZyypbYfFx4CbDlHjzi00WIajC7r6'
    item = Item.objects.get(pk=pk)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancel',
    )
    data = {
        'id': session.id
    }

    return JsonResponse(data, safe=False)


def item(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'main/item.html', {'item': item})


def items(request):
    items = Item.objects.all()
    return render(request, 'main/items.html', {'items': items})


def orders(request):
    orders = Order.objects.all()
    return render(request, 'main/orders.html', {'orders': orders})


def order(request, pk):
    order = Order.objects.get(pk=pk)
    disc = 0
    tax = 0
    if Discount.objects.filter(orders=order).exists():
        disc = Discount.objects.get(orders=order).discount
    if Tax.objects.filter(orders=order).exists():
        tax = Tax.objects.get(orders=order).tax
    return render(request, 'main/order.html', {'order': order, 'disc' : disc, 'tax': tax})


def buy_order(request, pk):
    stripe.api_key = 'sk_test_51MaQIsCGccPEKImWzia2XABWZFG7q2vIgHFlSK8KftR9ToxfLOv9ZwrIiqatvsSZoRaTKcZyypbYfFx4CbDlHjzi00WIajC7r6'
    order = Order.objects.get(pk=pk)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': order.currency,
                'product_data': {
                    'name': order.pk,
                },
                'unit_amount': int(order.total_price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
    )
    data = {
        'id': session.id
    }

    return JsonResponse(data, safe=False)
