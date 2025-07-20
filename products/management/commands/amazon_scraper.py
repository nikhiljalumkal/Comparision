import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Scrape Amazon product data"

    def handle(self, *args, **kwargs):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        url = "https://www.amazon.in/dp/B0CJBM9H8P"  # Sample URL
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        title = soup.find(id="productTitle")
        price = soup.find("span", {"class": "a-offscreen"})

        if title and price:
            print(f"Product: {title.get_text(strip=True)}")
            print(f"Price: {price.get_text(strip=True)}")
        else:
            print("Product or Price not found.")
