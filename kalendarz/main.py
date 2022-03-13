r_0 = 2024
m_0 = 1
d_0 = 1


r_n = int(input('Podaj rok:'))
m_n = int(input('Podaj miesiąc:'))
d_n = int(input('Podaj dzień:'))
print(d_n, m_n, r_n)

liczba_dni_w_miesiącu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
liczba_dni_od_początku_roku = 0

x = 1
while x < int(m_n):
    liczba_dni_od_początku_roku = liczba_dni_od_początku_roku + liczba_dni_w_miesiącu[x - 1]
    x = x + 1

liczba_dni_od_początku_roku_z_dniami = liczba_dni_od_początku_roku + d_n
print(liczba_dni_od_początku_roku)
print(liczba_dni_od_początku_roku_z_dniami)

if (r_0 > r_n and (r_0 - r_n) % 4 == 0 and (m_n == 1 and d_n <= 31) or (m_n == 2 and d_n <= 29)):
    liczba_dni_od_początku_roku_z_dniami = liczba_dni_od_początku_roku_z_dniami + 1

if ((r_0 < r_n) and ((r_n - r_0) % 4 == 0) and ((m_n == 1 and d_n >= 31) or (m_n == 2 and d_n >= 29))):
    liczba_dni_od_początku_roku_z_dniami = liczba_dni_od_początku_roku_z_dniami + 1

print(liczba_dni_od_początku_roku_z_dniami)

exeptions = [r_np for r_np in range(r_0, r_n + 1) if r_np % 100 == 0 and r_np % 400 != 0]
r_np = len(exeptions)

print(r_np)

if r_0 > r_n:
	l_dni = (((r_0 - r_n)//4)-r_np)*366 + (((r_0 - r_n)//4*3)+r_np)*365  - liczba_dni_od_początku_roku_z_dniami
elif r_0 < r_n:
	l_dni = (((r_n - r_0)//4)-r_np)*366 + (((r_n - r_0)//4*3)+r_np)*365  + liczba_dni_od_początku_roku_z_dniami
else:
	l_dni = liczba_dni_od_początku_roku_z_dniami
print(l_dni)

dni_tyg = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']

reszta = l_dni % 7
print(reszta)
print(dni_tyg[reszta])
