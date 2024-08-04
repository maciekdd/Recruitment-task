from product_service import ProductService
from utils import analyze_products

def main():
    base_url = "http://145.239.87.46:8000/product"
    service = ProductService(base_url)
    
    products = service.fetch_all_products()
    analyze_products(products)

if __name__ == "__main__":
    main()
