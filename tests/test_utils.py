from utils import analyze_products
from typing import List, Dict, Any

def test_analyze_products(capfd: Any):
    """
    Test that analyze_products prints correct analysis of product data.
    """
    products: List[Dict[str, Any]] = [
        {"product_id": 1, "product_name": "Cosmic Gizmo", "category": "Pet Supplies", "price": 10588.55},
        {"product_id": 2, "product_name": "Blackhole Gadget", "category": "Electronics", "price": 15366.36},
        {"product_id": 3, "product_name": "Stylish Outfit", "category": "Fashion", "price": 500.00},
        {"product_id": 4, "product_name": "Super Toy", "category": "Toys & Games", "price": 200.00},
        {"product_id": 5, "product_name": "Great Game", "category": "Toys & Games", "price": 300.00}
    ]

    analyze_products(products)

    captured = capfd.readouterr()
    assert "Total products: 5" in captured.out
    assert "Pet Supplies: 1" in captured.out
    assert "Electronics: 1" in captured.out
    assert "Fashion: 1" in captured.out
    assert "Toys & Games: 2" in captured.out
    assert "Most expensive product in Fashion: 3 - Stylish Outfit" in captured.out
    assert "Average price of Toys & Games products: 250.00 PLN" in captured.out
