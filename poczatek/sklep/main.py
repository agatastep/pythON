from symulator.orders import create_new_order


def run_shop():
print("hej, jestes w sklepie")
product_name = input("co chcesz kupic? ")
quantity = int(input("ile chcesz kupic? "))

result = create_new_order(product_name, quantity)
if result is not None:
    total_price = result["total_price"]
    print(f"łączny koszt wynosi {total_price} pln")

if __name__ == '__main__':
    run_shop()