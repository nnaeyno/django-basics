# Generated by Django 5.1.2 on 2024-10-09 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("title", models.CharField(max_length=100)),
                ("category_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategories",
                        to="store.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("product_image", models.ImageField(upload_to="products/")),
                ("categories", models.ManyToManyField(to="store.category")),
            ],
        ),
    ]
