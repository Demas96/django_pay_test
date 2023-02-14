from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Item(models.Model):
    rub, usd = 'RUB', 'USD'
    TYPES = [(rub, 'Рубли'), (usd, 'Доллар')]
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    currency = models.CharField(max_length=3, choices=TYPES, default=rub)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.price} {self.currency}'


class Order(models.Model):
    rub, usd = 'RUB', 'USD'
    TYPES = [(rub, 'Рубли'), (usd, 'Доллар')]
    items = models.ManyToManyField(Item)
    total_price = models.FloatField(null=True, blank=True, default=0)
    currency = models.CharField(max_length=3, choices=TYPES, default=rub)

    def __str__(self):
        self.total_price = 0
        for item in self.items.all():
            if item.currency == 'USD' and self.currency == 'RUB':
                self.total_price += item.price * 70
            elif item.currency == 'RUB' and self.currency == 'USD':
                self.total_price += item.price / 70
            else:
                self.total_price += item.price
        if Discount.objects.filter(orders=self).exists():
            self.total_price -= self.total_price * Discount.objects.get(orders=self).discount
        if Tax.objects.filter(orders=self).exists():
            self.total_price += self.total_price * Tax.objects.get(orders=self).tax
        self.save()
        return f'{self.pk} {self.total_price} {self.currency}'


class Discount(models.Model):
    orders = models.ManyToManyField(Order)
    discount = models.FloatField(default=0,
                            blank=True,
                            validators=[MinValueValidator(0), MaxValueValidator(1)])

    def __str__(self):
        return f'{self.discount}'


class Tax(models.Model):
    orders = models.ManyToManyField(Order)
    tax = models.FloatField(default=0,
                                 blank=True,
                                 validators=[MinValueValidator(0), MaxValueValidator(1)])
    def __str__(self):
        return f'{self.tax}'