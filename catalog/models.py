from django.db import models, connection
from django.db.models import IntegerField


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование товара')
    description = models.TextField (verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

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

    class Meta:
        verbose_name = 'пробукт'
        verbose_name_plural = 'пробукты'

    def __str__(self):
        return self.name



