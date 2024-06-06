import datetime
from django.db import models
from django.db.models import IntegerField


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование товара')
    description = models.TextField (verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование товара')
    description = models.TextField (verbose_name='Описание')
    image = models.ImageField(upload_to='product/photo', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = IntegerField(verbose_name='Цена ')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    manufactured_at = models.DateField(verbose_name='Дата производства продукта', default=datetime.date.today)

    class Meta:
        verbose_name = 'пробукт'
        verbose_name_plural = 'пробукты'

    def __str__(self):
        return self.name



