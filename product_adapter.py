from typing import Dict


class ProductAdapter:
    def __init__(self, product_data: Dict):
        self.product_data = product_data

    def to_dict(self) -> Dict:
        return {
            "product_id": self.product_data["product_id"],
            "product_name": self.product_data["product_name"],
            "category": self.product_data["category"],
            "price": self.product_data["price"]
        }
