# from .produkty import products
#
#
# def zamowienie(prod, ilosc, lista=None):
#     cena = products[prod][1] * ilosc
#     if lista is None:
#         lista = {}
#     lista[prod] = [ilosc, cena]
#     return lista
#
#
# bread = zamowienie('bread', 10)
# apples = zamowienie('apples', 25)
# lista_zamówień = bread | apples
# print(lista_zamówień)
#
# from symulator.zamowienie import zamowienie
#
# lista_zamowien = {}
# koszt = 0
# while True:
#     prod = input("podaj nazwe produktu: ")
#     ilosc = int(input("ilosc produktu: "))
#     if prod != 'x':
#         dodaj = zamowienie(prod, ilosc)
#         lista_zamowien = lista_zamowien | dodaj
#         koszt += lista_zamowien[prod][1]
#     else:
#         break
#
# print(f"{lista_zamowien} to łączny koszt {koszt}")
