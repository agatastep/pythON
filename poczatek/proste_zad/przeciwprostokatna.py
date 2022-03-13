import math


def przeciwprostokatna(a, b):
    return math.sqrt(math.pow(a,2) + math.pow(b,2))


a = float(input("pierwszy bok: "))
b = float(input("drugi bok: "))
print(f"przeciwprostokatna ma dlugosc {przeciwprostokatna(a,b)}")



