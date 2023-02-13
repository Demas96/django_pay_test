from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Item
import stripe

def buy(request, pk):
    stripe.api_key = 'sk_test_51MaQIsCGccPEKImWzia2XABWZFG7q2vIgHFlSK8KftR9ToxfLOv9ZwrIiqatvsSZoRaTKcZyypbYfFx4CbDlHjzi00WIajC7r6'
    item = Item.objects.get(pk=pk)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
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


def item(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'main/item.html', {'item': item})
