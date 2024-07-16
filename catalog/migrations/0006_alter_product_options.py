# Generated by Django 4.2.2 on 2024-07-16 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "permissions": [
                    (
                        "can_cancel_publication",
                        "may cancel the publication of the product",
                    ),
                    (
                        "can_change_description ",
                        "can change the description of any product",
                    ),
                    ("can_cancel_category", "can change the category of any product"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]