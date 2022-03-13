import predkosc_funkcja

s = float(input("podaj droge: "))
t = float(input("podaj czas: "))

predkosc_funkcja.v(s, t)

predkosc = predkosc_funkcja.v(s, t)
print(f"biegles z predkoscia {predkosc:.2f}km/h")
