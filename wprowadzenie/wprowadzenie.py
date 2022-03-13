# '1'
# s = 38
# t = 3
# v = s / t
# print(v)
# print("on biegł z prędkością", v, "km/h")
#
# '2'
# wart_pocz = 1000
# proc = 4
# t = 5
# wart_kon = wart_pocz * (1 + proc/100) ** t
# print(wart_kon)
#
# '3'
# a = 9
# b = 12
# c = (a ** 2 + b ** 2) ** 0.5
# s = int(2*c) * "-"
# print(s)
#
# '4'
# print("moje ulubione potrawy to: ", "dupka", "kupka", "kanapka", sep = "\n\t")
#
# '5'
# lat = input("ile masz lat?")
# lat = int(lat)
# mies = lat * 12
# print("twój wiek to", mies, "miesięcy")
#
# '6'
# dist = input("ile km przeszedłeś w tym tyg?")
# dist = int(dist)
# tyg = 40075 / dist
# print("okrążysz ziemię w", tyg, "tygodni")
#
# '7'
# wart_pocz = input("początkowa wartość:")
# proc = input("oprocentowanie:")
# t = input("czas trwania w latach:")
# wart_pocz = int(wart_pocz)
# proc = int(proc)
# t = int(t)
# wart_kon = wart_pocz * (1 + proc/100) ** t
# print("po", t, "latach będziesz mieć", wart_kon:.2f, "przy oprocentowaniu", proc)
#
# '8'
# l = input("ile kosztują jabłka w lidlu?")
# b = input("ile kosztują jabłka w biedrze?")
# ż = input("ile kosztują jabłka w żabce?")
# mini = min(l, b, ż)
# print("najtansze jablka kosztują", mini)

# '9'
# wart_pocz = input("początkowa wartość:")
# proc = input("oprocentowanie:")
# t = input("czas trwania w latach:")
# wart_pocz = int(wart_pocz)
# proc = int(proc)
# t = int(t)
# wart_kon = wart_pocz * (1 + proc/100) ** t
# print(f"po {t} latach będziesz mieć {wart_kon:.2f}")
#
# '10'
# imie = input("podaj imie ")
# print(len(imie))
#
# '11'
# city = input("w jakim miescie mieszkasz? ")
# print(f"jak milo ze mieszkasz w {city.title()}")
#
# '12'
# ford = "ab100100"
# audi = "EEE 123123"
# citroen = "Zk-300300"
# honda = "AB210210"
# print(ford.upper(), audi.replace(' ', ''), citroen.upper().replace('-', ''), honda, sep = "\n")
#
# '13'
# favourite_sports = [
#     'chuj',
#     'gowno',
#     'miod'
# ]
# pierwszy = favourite_sports[0]
# ostatni = favourite_sports[2]
# print(f"ulubiony to {pierwszy} a ostatni to {ostatni}")
# favourite_sports[0] = 'cipcia'
# print(favourite_sports)
#
# '14'
# food = input("jakie są twoje 3 ulubiensze jedzonki? ")
# print(food.split(", "))
#
# '15'
# tel = input("podaj tel ")
# print(type(tel))
# a = tel[:6]
# b = len(tel[6:])
# print(f"{a}{b * '-'}")

# '16'
# szkola = {
#     "matma" : [4, 5, 4],
#     "polak" : [3, 4, 2],
#     "przyrka" : [5, 5]
# }
# print(szkola)
#
# '17'
# my_family =
#     {
#         "imie": "agata",
#         "nazwisko" : "stepien",
#         "uro" : "1 paź 1996",
#         "rodzice" : [
#             {
#                 "imie": "marta",
#                 "nazwisko": "stepien",
#                 "uro": "1 cze 1962",
#             },
#             {
#                 "imie": "pawel",
#                 "nazwisko": "stepien",
#                 "uro": "29 sie 1961"
#             }
#     ]
#     }
# 
# print(my_family)

# '18'
# food = input("ile wydajesz na food ")
# food = float(food)
# fun = input("ile wydajesz na fun ")
# fun = float(fun)
# cost = input("ile wydajesz na cost ")
# cost = float(cost)
# other = input("ile wydajesz na other ")
# other = float(other)
# suma = food + fun + cost + other
# cat = {
#     "food" : food/suma * 100,
#     "fun" : fun/suma * 100,
#     "cost" : cost/suma * 100,
#     "other" : other/suma * 100
# }
# kat = input("wybierz kategorie ")
# print(f"procentowy udział wynosi {cat[kat]} %")
#
# '19'
# j = input("ile kosztują jabłka? ")
# g = input("ile kosztują gruszki? ")
# a = input("ile kosztują arbuzy? ")
# print(f'czy jablka sa droższe niż gruszki? {j > g}')
# print(f'czy arbuzy sa droższe niż gruszki? {a > g}')
# print(f'czy jablka sa droższe niż arbuzy? {j > a}')
#
# '20'
# lista = input("podaj liste zakupów: ")
# lista = lista.split()
# print(lista)
# result = len(lista) >= 3
# print(f"czy ta lista jest długa? {result}")
#
# '21'
# wart_pocz = input("początkowa wartość:")
# proc = input("oprocentowanie:")
# t = input("czas trwania w latach:")
# wart_pocz = int(wart_pocz)
# proc = int(proc)
# t = int(t)
# wart_kon = wart_pocz * (1 + proc/100) ** t
# result = wart_kon >= wart_pocz * 1.1
# print(f"po {t} latach będziesz mieć {wart_kon:.2f}")
# print(f"czy w planowanym okresie łączna wartość inwestycji wzrośnie o co najmniej 10%? {result}")
#
# '22'
# j = float(input("ile kosztują jabłka? "))
# g = float(input("ile kosztują gruszki? "))
# a = float(input("ile kosztują arbuzy? "))
# if j > g:
#     print(f'jablka sa droższe niż gruszki')
# else:
#     print(f'jablka sa tańsze niż gruszki lub kosztują tyle samo')
#
# '23'
# wart_pocz = input("początkowa wartość:")
# proc = input("oprocentowanie:")
# t = input("czas trwania w latach:")
# wart_pocz = int(wart_pocz)
# proc = int(proc)
# t = int(t)
# wart_kon = wart_pocz * (1 + proc/100) ** t
# result = wart_kon >= wart_pocz * 1.1
# print(f"po {t} latach będziesz mieć {wart_kon:.2f}")
# if wart_kon >= wart_pocz * 1.1:
#     print(f"łączna wartość inwestycji wzrośnie o co najmniej 10%")
# else:
#     print(f"łączna wartość inwestycji nie wzrosła o co najmniej 10%")
#
# '24'
# food = float(input("ile wydajesz na food "))
# fun = float(input("ile wydajesz na fun "))
# cost = float(input("ile wydajesz na cost "))
# other = float(input("ile wydajesz na other "))
#
# suma = food + fun + cost + other
# cat = {
#     "food" : food/suma * 100,
#     "fun" : fun/suma * 100,
#     "cost" : cost/suma * 100,
#     "other" : other/suma * 100
# }
# maks = None
#
# if cat["food"] > cat["fun"]:
#     maks = cat["food"]
# else:
#     maks = cat["fun"]
# if maks < cat["cost"]:
#     maks = cat["cost"]
# if maks < cat["other"]:
#     maks = cat["other"]
#
# print(f"maksymalna kategoria to {maks}")
#
# '25'
# mat = float(input("jaką ocenke masz z mat? "))
# chem = float(input("jaką ocenke masz z chem? "))
# fiz = float(input("jaką ocenke masz z fiz? "))
# sr = (mat + chem + fiz) / 3
#
# if mat != 1:
#     if chem != 1:
#         if fiz != 1:
#             print("nie masz zadnej 1 więc zdałeś")
#         else:
#             print("nie zdajesz")
#
# if sr > 3.5:
#     if mat == 1:
#         if chem != 1:
#             if fiz != 1:
#                 print("masz co prawda 1 ale sr większa niż 3.5 wiec zdajesz")
#             else:
#                 print("nie zdajesz")
#     if chem == 1:
#         if mat != 1:
#             if fiz != 1:
#                 print("masz co prawda 1 ale sr większa niż 3.5 wiec zdajesz")
#             else:
#                 print("nie zdajesz")
#     if fiz == 1:
#         if chem != 1:
#             if mat != 1:
#                 print("masz co prawda 1 ale sr większa niż 3.5 wiec zdajesz")
#             else:
#                 print("nie zdajesz")
# else:
#     print("nie zdajesz")
#lepsze rozwiązanie:

# mat = float(input("jaką ocenke masz z mat? "))
# chem = float(input("jaką ocenke masz z chem? "))
# fiz = float(input("jaką ocenke masz z fiz? "))
# sr = (mat + chem + fiz) / 3
# fail = 0
# if mat == 1:
#     fail = fail +1
# if chem == 1:
#     fail = fail + 1
# if fiz == 1:
#     fail = fail + 1
# if fail == 0:
#     print("nie masz zadnej 1 więc zdałeś")
# if fail == 1:
#     if sr > 3.5:
#         print("masz co prawda 1 ale sr większa niż 3.5 wiec zdajesz")
#     else:
#         print("nie zdałeś")
# if fail > 1:
#     print("nie zdałeś")


# '26'
# imie = input("podaj swe imie: ")
# if imie[-1] == "a":
#     print("jestes kobieta woda ogniem burza perla na dnieeee")
# else:
#     print("u r dude cock dick")

# '27'
# kwota_kred = float(input("ile chcesz kredytu? "))
# oproc = float(input("ile chcesz oprocentowania? "))
# wklad_własny = float(input("ile dasz wkładu własnego? "))
# czas = float(input("na ile chcesz ten kredyt w latach? "))
# przychod = float(input("ile miesiecznego przychodu masz? "))
# wydatki = float(input("ile miesicznie masz wydatkow? "))
# rata = (kwota_kred * oproc / 100) / 12 + kwota_kred / (czas * 12)
# dostepne_srodki = przychod - wydatki
# wart_nieruch = wklad_własny + kwota_kred
#
# if wart_nieruch <= wklad_własny + kwota_kred and rata <= dostepne_srodki:
#     print("stac cie na kredyt")
# else:
#     print("nie stac cie na kredyt")
#
# inne warunki:

# kwota_kred = float(input("ile chcesz kredytu? "))
# oproc = float(input("ile chcesz oprocentowania? "))
# wklad_własny = float(input("ile dasz wkładu własnego? "))
# czas = float(input("na ile chcesz ten kredyt w latach? "))
# przychod = float(input("ile miesiecznego przychodu masz? "))
# wydatki = float(input("ile miesicznie masz wydatkow? "))
# rata = (kwota_kred * oproc / 100) / 12 + kwota_kred / (czas * 12)
# dostepne_srodki = przychod - wydatki
# wart_nieruch = wklad_własny + kwota_kred
#
# if wklad_własny > 0.2 * wart_nieruch and dostepne_srodki + 1000 >= rata:
#     print("dostaniesz")
# if 0.1 * wart_nieruch < wklad_własny < 0.2 * wart_nieruch and dostepne_srodki + 2000 >= rata:
#     print("dostaniesz")
# if wklad_własny < 0.1 * wart_nieruch:
#     print("nie dostaniesz")
#
# ładniej:
# kwota_kred = float(input("ile chcesz kredytu? "))
# oproc = float(input("ile chcesz oprocentowania? "))
# wklad_własny = float(input("ile dasz wkładu własnego? "))
# czas = float(input("na ile chcesz ten kredyt w latach? "))
# przychod = float(input("ile miesiecznego przychodu masz? "))
# wydatki = float(input("ile miesicznie masz wydatkow? "))
# rata = (kwota_kred * oproc / 100) / 12 + kwota_kred / (czas * 12)
# dostepne_srodki = przychod - wydatki
# wart_nieruch = wklad_własny + kwota_kred
# wklad_do_wart = wklad_własny / wart_nieruch
# bufor = dostepne_srodki - rata
# war1 = wklad_do_wart > 0.2 and bufor > 1000
# war2 = 0.1 < wklad_do_wart < 0.2 and bufor > 2000
# if war1 or war2:
#     print("masz to")
# else:
#     print("nie masz tego")
#
# '28'
# co = input("wybierz wartość_lokaty lub zdolność_kredytowa: ")
# if co == "wartość_lokaty":
#     wart_pocz = input("początkowa wartość:")
#     proc = input("oprocentowanie:")
#     t = input("czas trwania w latach:")
#     wart_pocz = int(wart_pocz)
#     proc = int(proc)
#     t = int(t)
#     wart_kon = wart_pocz * (1 + proc/100) ** t
#     print(f"po {t} latach będziesz mieć {wart_kon:.2f}")
# elif co == "zdolność_kredytowa":
#     kwota_kred = float(input("ile chcesz kredytu? "))
#     oproc = float(input("ile chcesz oprocentowania? "))
#     wklad_własny = float(input("ile dasz wkładu własnego? "))
#     czas = float(input("na ile chcesz ten kredyt w latach? "))
#     przychod = float(input("ile miesiecznego przychodu masz? "))
#     wydatki = float(input("ile miesicznie masz wydatkow? "))
#     rata = (kwota_kred * oproc / 100) / 12 + kwota_kred / (czas * 12)
#     dostepne_srodki = przychod - wydatki
#     wart_nieruch = wklad_własny + kwota_kred
#     wklad_do_wart = wklad_własny / wart_nieruch
#     bufor = dostepne_srodki - rata
#     war1 = wklad_do_wart > 0.2 and bufor > 1000
#     war2 = 0.1 < wklad_do_wart < 0.2 and bufor > 2000
#     if war1 or war2:
#         print("masz to")
#     else:
#         print("nie masz tego")
# else:
#     print('nic nie wybrales to nic dostales')
#
# '29'

# wiek = int(input("wiek: "))
# płeć = input("płeć: ")
# wynik = int(input("wynik: "))
#
# if 20 < wiek <= 29:
#     if płeć == "M":
#         if wynik > 2800:
#             print("bardzo dobrze")
#         elif 2400 < wynik:
#             print("dobrze")
#         elif 2200 < wynik:
#             print("średnio")
#         elif 1600 < wynik:
#             print("źle")
#         else:
#             print("bardzo źle")
#     if płeć == "K":
#         if wynik > 2700:
#             print("bardzo dobrze")
#         elif 2200 < wynik:
#             print("dobrze")
#         elif 1800 < wynik:
#             print("średnio")
#         elif 1500 < wynik:
#             print("źle")
#         else:
#             print("bardzo źle")
#
# '30'
#
# lista = input("podaj liste zakupów: ")
# lista = lista.split(",")
# print(lista)
# if "bułki" in lista or "chleb" in lista:
#     print(f"ta lista zawiera chleb lub bułki")
# else:
#     print(f"brak chleb lub bułki")
#
# '31'
# tel = input("podaj tel: ")
# if "0" in tel:
#     print("zawiera chociaz jedno 0")
# else:
#     print("nie zawiera 0")
#
# '32'
# value = "agatka"
# if value:
#     print("agatka jest prawdą")
# elif not value:
#      print("agatka jest fałszem")
# elif value is None:
#     print("agatka jest pusta")
# else:
#     print("agatka jest kimś innym")

# testy
# print(value == True)
# print(bool("agatka"))
# print(bool(9))
# value = 9
# if value == True:
#     print("agatka jest prawdą")
# elif value == False:
#     print("agatka jest fałszem")
# elif value == None:
#     print("agatka jest pusta")
# else:
#     print("agatka jest kimś innym")
#
# print(value == True)

# '33'
# liczba = int(input("podaj liczbe: "))
# count = 1
# while count < 10:
#     if liczba % 2 == 0:
#         print("dzięki")
#         count += 9
#     else:
#         print("ponów próbę")
#         liczba = int(input("podaj liczbe: "))
#         count += 1
#
# '34'
#
# tel = input("podaj nr tel: ")
# tel = tel.replace("-", "")
# tel = tel.replace(" ", "")
# i = 0
# formatted = ""
# while i < len(tel):
#     if i % 3 == 0 and i != 0:
#         formatted += "-" + tel[i]
#         i += 1
#     else:
#         formatted += tel[i]
#         i += 1
# print(formatted)

# '35'
# food = input("napisz ulubione dania rozdzielając przecinkiem: ")
# print(food.split(","))
# food = food.split(",")
# i = 0
# while i < len(food):
#     print (f"{i} -> {food[i]}")
#     i += 1
#
# '36'
# oceny = input("wprowadz oceny: ")
# oceny = oceny.split(",")
# print(oceny)
# print(len(oceny))
# grades = ""
# index = 0
# while index < len(oceny) + 1:
#     ocena = input("wprowadz ocene: ")
#     grades += ocena
#     index += 1
#     if ocena == 'X':
#         print('dziekuje za oceny')
# print(grades)
# grades = list(grades)
# print(grades)
# print(grades[:-1])
# grades = grades[:-1]

# '36a'
#
# grades = []
# cont = True
# while cont:
#     grade = input('podaj ocene: ')
#     if grade != 'X':
#         grades.append(grade)
#     else:
#         cont = False
#         print(grades)
#
# suma = 0
# for grade in grades:
#     suma += int(grade)
#
# average = (suma/len(grades))
# print(round(average, 2))
#
# '37'
# tel = input('podaj nr tel: ')
# formatted_tel = ''
# for index, number in enumerate(tel):
#     if index % 3 == 0 and index != 0:
#         formatted_tel += '-' + number
#     else:
#         formatted_tel += number
# print(formatted_tel)
#
# '38'
# jedzenie = []
# hobby = []
# bilety = []
# cont = True
# food = ''
# while cont:
#     food = input(f'podaj food: ')
#     if food != 'x':
#         jedzenie.append(food)
#     else:
#         print(jedzenie)
#
# nie no musisz to zrobic ze słownikim
#
# expenditures = {
#                 "food":[30, 17, 50],
#                 "hobby":[100, 100],
#                 "ticket":[3, 3, 3]
#                 }
# cont = True
# while cont:
#     food = input("wprowadz wydatki na food: ")
#     food = [int(n) for n in food.split(',')]
#     food = [int(item) for item in food]
#     expenditures["food"].extend(food)
#     hobby = input("wprowadz wydatki na hobby: ")
#     hobby = [int(n) for n in hobby.split(',')]
#     hobby = [int(item) for item in hobby]
#     expenditures["hobby"].extend(hobby)
#     ticket = input("wprowadz wydatki na ticket: ")
#     ticket = [int(n) for n in ticket.split(',')]
#     ticket = [int(item) for item in ticket]
#     expenditures["ticket"].extend(ticket)
#     new = input("wprowadz nową kategorię: ")
#     if new != 'x':
#         expenditures["new"] = []
#         newv = input("wprowadz wydatki na new: ")
#         newv = [int(n) for n in newv.split(',')]
#         newv = [int(item) for item in newv]
#         expenditures["new"].extend(newv)
#         print(expenditures)
#         cont = False
#     else:
#         print(expenditures)
#         cont = False
#
# list = []
# for key in expenditures:
#     list.append(sum(expenditures[key]))
# print(list)
#
#
#
# total = sum(list)
# udzialy = []
# najwieksze = 0
# max_index = 0
# for index, value in enumerate(list):
#     udzial = round((value/total) * 100, 2)
#     if udzial > najwieksze:
#         najwieksze = udzial
#         max_index = index
#     udzialy.append(udzial)
# print(udzialy)
# print(max_index, najwieksze)
# # tak jest prościej bo od razu robię na słowniku a nie muszę brac indexu z listy i szukac dla tego indeksu kategorii w słowniku
# expenditures2 = expenditures
# for key in expenditures2:
#     expenditures2[key] = sum(expenditures2[key])
# print(expenditures2)
# print(max(expenditures2, key = expenditures2.get))
#
# '39'
# tel = input('podaj nr tel: ')
# for i in range(10):
#     i = str(i)
#     ilosc = tel.count(i)
#     print(ilosc)

# print(f"zer jest {tel.count('0')}, jedynek jest {tel.count('1')}")
# '40'
# wart_kred = int(input("wartość kredytu:"))
# proc = float(input("oprocentowanie:"))
# t = int(input("czas trwania w latach:"))
# koszty_pocz = int(input("koszty początkowe:"))
#
# miesieczny_kapital = wart_kred / (t * 12)
#
# cena = 0
# suma_rat = 0
# for num in range(1, (t * 12) + 1):
#     pozost_kapit = wart_kred - (num - 1) * miesieczny_kapital
#     rata = (pozost_kapit * proc / 100) / 12 + miesieczny_kapital
#     suma_rat += rata
#
# print(suma_rat)
# cena = suma_rat + koszty_pocz - wart_kred
# print(cena)
# print(suma_rat + koszty_pocz)
#
# '41'
# grades = input("podaj oceny: ")
# grades = grades.split(",")
# print(grades)
# for i in grades:
#     if int(i) == 1:
#         print("powtarzasz klase!")
#         break
# else:
#     print("gratuluje!")
#
# '42'
#
# wydatki = {}
# i = ''
#
# while True:
#     i = input("podaj kategorię: ")
#     if i != 'x':
#         wydatki[i] = []
#         cost = input("podaj kwoty i zakończ iksem: ")
#         cost = cost.split(',')
#     else:
#         break
#     for c in cost:
#         if c != "x":
#             wydatki[i].append(int(c))
#         else:
#             break
#
# print(wydatki)
#
# najw = 0
# indeks_najw = ''
# print(wydatki)
# for i in wydatki:
#     wydatki[i] = sum(wydatki[i])
#     if wydatki[i] > najw:
#         najw = wydatki[i]
#         indeks_najw = i
# print(najw, indeks_najw)
# print(wydatki)
# print(f"największy udział ma {indeks_najw}")
# total = sum(wydatki.values())
# print(total)
#
# for n in wydatki:
#     wydatki[n] = wydatki[n] * 100 / total
# print(wydatki)

# przyklad
# wydatki = {
#     'bub': ['1','2'],
#     'buba': ['2','33']
# }
#
# for n in wydatki:
#     for i, v in enumerate(wydatki[n]):
#         wydatki[n][i] = int(v)
#
# print(wydatki)

# '43'

# liczby = input("podaj liczby: ")
# liczby = list(map(int, liczby))
# print(liczby)
# for i in liczby:
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# '44'
#
# def pole(a, b):
#     pole = a * b
#     print(pole)
#     return pole
#
# print(pole(5, 2))
#
# '45'

# def v(s, t):
#     v = s / t
#     print(v)
#     return(v)
#
# bieg_droga = int(input("podaj droge biegu: "))
# bieg_czas = int(input("podaj czas biegu: "))
# print(f"twoja prędkość biegu to {v(bieg_droga, bieg_czas)}")
#
# '46'
# a = {"buba" : [2, 4, 12], "chuj" : [1, 77]}
# slownik = {}
# kat = input("podaj kat lub x: ")
# while kat != 'x':
#     slownik[kat] = []
#     wyd = input("podaj wyd lub x: ")
#     while wyd != "x":
#         slownik[kat].append(int(wyd))
#         wyd = input("podaj wyd lub x: ")
#     else:
#         kat = input("podaj kat lub x: ")
# else:
#     print(slownik)
#
# slownik = {}
# stop = True
# wyd = True
# while stop:
#     kat = input("podaj kat lub x: ")
#     if kat != "x":
#         slownik[kat] = []
#         while wyd:
#             wyd = input("podaj wyd lub x: ")
#             if wyd != 'x':
#                 slownik[kat].append(int(wyd))
#             else:
#                 break
#     else:
#         stop = False
#
# print(slownik)

# def wydatki(slownik):
#     suma = []
#     print(slownik)
#     for n in slownik:
#         slownik[n] = sum(slownik[n])
#         suma.append(slownik[n])
#     print(sum(suma))
#     print(slownik)
#     udzialy = []
#     for n in slownik:
#         udzial = slownik[n] / sum(suma) * 100
#         udzialy.append(udzial)
#     print(udzialy)
#     m = 0
#     if slownik[n] > m:
#         max_wyd = n
#         return(max_wyd)
#
# print(wydatki(slownik))

# inaczej
#
# def load_expenditures(category_name):
#     expenditures_values = []
#     while True:
#         expenditure = input(f"podaj wydatek na kategorie {category_name} lub x by zakonczyc: ")
#         if expenditure == 'x':
#             return expenditures_values
#         expenditure_value = float(expenditure)
#         expenditures_values.append(expenditure_value)
#
#
# def load_expenditures_by_category():
#     expenditures = {}
#     while True:
#         category_name = input("podaj kategorie wydatkow lub zakoncz x: ")
#         if category_name == 'x':
#             return expenditures
#         expenditures[category_name] = load_expenditures(category_name)
#
#
#
# def calculate_total_expenditures(expenditures):
#     result = 0
#     for n in expenditures.values():
#         result += sum(n)
#     return result
#
#
# def calculate_expenditures_percentages(expenditures, total_expenditures):
#     percentages_by_category_name = {}
#     for category_name, category_expenditures in expenditures.items():
#         total_category_expenditures = sum(category_expenditures)
#         percentages_by_category_name[category_name] = total_category_expenditures * 100 / total_expenditures
#     return percentages_by_category_name
#
#
# def find_most_important_category(percentages_by_category_name):
#     highest_percentage_category = None
#     highest_percentage = 0
#     for category, percentage in percentages_by_category_name.items():
#         if percentage > highest_percentage:
#             highest_percentage = percentage
#             highest_percentage_category = category
#     return highest_percentage_category, highest_percentage
#
#
# def print_most_important_category_info(category, percentage):
#     print(f"najwiekszy udzial ma {category} wynoszący {percentage:.0f}%")
#
#
# def print_category_info(category, percentage):
#     print(f"na {category} wydajesz {percentage:.0f}% wszystkich wydatkow")
#
#
# expenditures_by_category = load_expenditures_by_category()
# total_expenditures = calculate_total_expenditures(expenditures_by_category)
# expenditures_percentage = calculate_expenditures_percentages(expenditures_by_category, total_expenditures)
# most_important_category, most_important_category_percentage = find_most_important_category(expenditures_percentage)
#
#
# if most_important_category is not None:
#     print_most_important_category_info(most_important_category, most_important_category_percentage)
#
#
# for category, percentage in expenditures_percentage.items():
#     print_category_info(category, percentage)

# '47'

# def v(s, t):
#     v = s / t
#     print(v)
#     return(v)
#
# bieg_droga = int(input("podaj droge biegu: "))
# bieg_czas = int(input("podaj czas biegu: "))
# print(f"twoja prędkość biegu to {v(s=bieg_droga, t=bieg_czas):.2f}km/h")
# print(f"twoja inna prędkość biegu to {v(s=40, t=7):.2f}km/h")
#
# inaczej
#
# def v(s, t):
#     v = s / t
#     return(v)
#
# def kalkulator(pojazd):
#     droga = float(input("podaj droge: "))
#     czas = float(input("podaj czas: "))
#     print(f"twoja prędkość przy pomocy {pojazd} to {v(s=droga, t=czas):.2f}km/h")
#     return v
#
# print(kalkulator(pojazd='rower'))
#
# '48'
#
# def nazwa(imie):
#     return(imie)
#
# imie = 'agata'
# print(imie)
# print(nazwa('mary'))
# print(imie)

# pies = 'burek'
#
# def zwierz():
#     global pies
#     pies = 'azor'
#     return pies
#
# print(pies)
# print(zwierz())
# print(pies)
#
# '49'
#
# def przedzial(liczba, zakres=0.1):
#     amplituda = liczba * zakres
#     dol = liczba - amplituda
#     gora = liczba + amplituda
#     return dol, gora
#
# print(przedzial(10))
#
# '50'
# nowi = input("kto sie zapisał? ")
#
#
# def uczestnicy(new, starzy=None):
#     if starzy is None:
#         starzy = []
#     starzy.extend(list(new.split(",")))
#     return starzy
#
#
# print(uczestnicy(nowi, ['maja','hania']))
#
# lepsze nazwy

# nowi = input("kto sie zapisał? ")
#
#
# def list_connection(list1, list2=None):
#     if list2 is None:
#         list2 = []
#     list2.extend(list(list1.split(",")))
#     return list2
#
#
# uczestnicy = 'ania,marek'
# monday = list_connection(uczestnicy)
# print(monday)
# uczestnicy = 'jan,ban'
# monday = list_connection(uczestnicy, list2=monday)
# print(monday)

#
# print(list_connection(nowi, ['maja','hania']))
#
