from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('items/', views.items, name='items'),
    path('orders/', views.orders, name='orders'),
    path('buy/<int:pk>', views.buy),
    path('buy_order/<int:pk>', views.buy_order),
    path('item/<int:pk>', views.item),
    path('order/<int:pk>', views.order),
    path('cancel/', views.cancel, name='cancel'),
    path('success/', views.success, name='success'),
]