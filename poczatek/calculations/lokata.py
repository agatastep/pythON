import calculations.kalk_lokaty
print(__name__)
i = int(input("initial value: "))
p = float(input("percentage: "))
t = int(input("time: "))

value = calculations.kalk_lokaty.lokata(i, p, t)
print(f"wart lokaty to {value:.2f}")