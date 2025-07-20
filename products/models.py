from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_url = models.URLField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.price} on {self.date}"
