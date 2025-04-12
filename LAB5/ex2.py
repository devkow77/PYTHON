import json

list_of_products = [
    {"name": "Apple", "price": 1.24, "available": True},
    {"name": "Grape", "price": 1.56, "available": False},
    {"name": "Pear", "price": 0.97, "available": True},
    {"name": "Bannana", "price": 2.54, "available": False}
]

# serialize and deserialize object
with open("list_of_products_in_bytes.json", "w") as file:
    json.dump(list_of_products, file, indent=4)
with open("list_of_products_in_bytes.json", "r") as file:
    data_loaded = json.load(file)

for product in data_loaded:
    print(product)



