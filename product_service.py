import requests
from exponential_backoff import ExponentialBackoff
from product_adapter import ProductAdapter
from typing import List, Dict


class ProductService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.backoff_strategy = ExponentialBackoff()

    def fetch_product(self, token: str = None) -> Dict:
        url = self.base_url
        if token:
            url += f"?next_product_token={token}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def fetch_all_products(self) -> List[Dict]:
        products = []
        token = None

        while True:
            product_data = self.backoff_strategy.execute(lambda: self.fetch_product(token))
            products.append(ProductAdapter(product_data).to_dict())
            token = product_data.get("next_product_token")
            if not token:
                break

        return products
