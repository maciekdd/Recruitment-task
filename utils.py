from typing import List, Dict


def analyze_products(products: List[Dict]) -> None:
    total_products = len(products)
    print(f"Total products: {total_products}")

    categories = {}
    for product in products:
        category = product["category"]
        if category not in categories:
            categories[category] = 0
        categories[category] += 1

    print("Products in each category:")
    for category, count in categories.items():
        print(f"{category}: {count}")

    most_expensive_fashion = max(
        (p for p in products if p["category"] == "Fashion"),
        key=lambda p: p["price"],
        default=None
    )

    if most_expensive_fashion:
        print(
            f"Most expensive product in Fashion: {most_expensive_fashion['product_id']} - {most_expensive_fashion['product_name']}")

    toys_and_games = [p["price"] for p in products if p["category"] == "Toys & Games"]
    if toys_and_games:
        average_price = sum(toys_and_games) / len(toys_and_games)
        print(f"Average price of Toys & Games products: {average_price:.2f} PLN")
