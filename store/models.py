from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subcategories",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    def get_main_category(self):
        if self.parent:
            return self.parent.get_main_category()
        return self.title, self.category_id

    def get_direct_category(self):
        if self.parent:
            return self.parent.title, self.parent.category_id
        return None, None


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    categories = models.ManyToManyField(Category)
    product_id = models.AutoField(primary_key=True)
    product_image = models.ImageField(upload_to="store/product_images/")

    def __str__(self):
        return self.name
