from product_adapter import ProductAdapter


def test_product_adapter():
    """
    Test that ProductAdapter correctly adapts product data to dictionary.
    """
    product_data = {
        "product_id": 1,
        "product_name": "Cosmic Gizmo",
        "category": "Pet Supplies",
        "price": 10588.55
    }
    adapter = ProductAdapter(product_data)
    adapted_product = adapter.to_dict()

    assert adapted_product["product_id"] == 1
    assert adapted_product["product_name"] == "Cosmic Gizmo"
    assert adapted_product["category"] == "Pet Supplies"
    assert adapted_product["price"] == 10588.55
