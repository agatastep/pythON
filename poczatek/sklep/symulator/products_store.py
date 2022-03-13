products = {
    "bread": {
        "quantity": 100,
        "price": 3.5
    },
    "apples": {
        "quantity": 50,
        "price": 3.2
    }
}


def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity
