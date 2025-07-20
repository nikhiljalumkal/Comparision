import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from products.models import Store, Product, PriceHistory

class Command(BaseCommand):
    help = "Scrape Amazon product data and save to DB"

    def handle(self, *args, **kwargs):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        url = "https://www.amazon.in/dp/B0CJBM9H8P"  # Sample URL
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        title = soup.find(id="productTitle")
        price = soup.find("span", {"class": "a-offscreen"})
        image = soup.find("img", {"id": "landingImage"})

        if title and price:
            name = title.get_text(strip=True)
            price_value = float(price.get_text(strip=True).replace("₹","").replace(",",""))
            image_url = image['src'] if image else ''

            store, created = Store.objects.get_or_create(name="Amazon", website="https://www.amazon.in")

            # Create or update Product
            product, created = Product.objects.update_or_create(
                product_url=url,
                defaults={
                    'name': name,
                    'current_price': price_value,
                    'store': store,
                    'image_url': image_url,
                }
            )

            # Add to price history
            PriceHistory.objects.create(product=product, price=price_value)

            print(f"{'Created' if created else 'Updated'}: {name} at ₹{price_value}")

        else:
            print("Product or Price not found.")
