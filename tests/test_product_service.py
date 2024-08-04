import pytest
from product_service import ProductService
from unittest.mock import patch
from typing import Generator


@pytest.fixture
def service():
    """
    Fixture to provide a ProductService instance.
    """
    yield ProductService("http://145.239.87.46:8000/product")


@patch("product_service.ProductService.fetch_product")
def test_fetch_all_products(mock_fetch_product: Generator, service: ProductService):
    """
    Test that ProductService fetches all products correctly.
    """
    mock_fetch_product.side_effect = [
        {"product_id": 1, "product_name": "Cosmic Gizmo", "category": "Pet Supplies", "price": 10588.55,
         "next_product_token": "token1"},
        {"product_id": 2, "product_name": "Blackhole Gadget", "category": "Electronics", "price": 15366.36,
         "next_product_token": ""}
    ]
    products = service.fetch_all_products()
    assert len(products) == 2
    assert products[0]["product_name"] == "Cosmic Gizmo"
    assert products[1]["product_name"] == "Blackhole Gadget"
