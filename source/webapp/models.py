from django.db import models

PRODUCT_OTHER_CHOICE = 'other'
PRODUCT_CATEGORY_CHOICES = (
    (PRODUCT_OTHER_CHOICE, 'Другое'),
    ('book', 'Книга'),
    ('toy', 'Игрушка'),
    ('cloth', 'Одежда'),
    ('shoe', 'Обувь')
)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=2000, verbose_name='Описание', null=True, blank=True)
    category = models.CharField(max_length=20, verbose_name='Категория',
                                choices=PRODUCT_CATEGORY_CHOICES, default=PRODUCT_OTHER_CHOICE)
    amount = models.IntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name


