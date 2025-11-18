import json
from .models import Customer, Product

def load_seed(path):
    with open(path) as f:
        data = json.load(f)
    for c in data.get("customers", []):
        Customer(**c).save()
    for p in data.get("products", []):
        Product(**p).save()
