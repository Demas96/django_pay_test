from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:pk>', views.buy),
    path('item/<int:pk>', views.item),
]