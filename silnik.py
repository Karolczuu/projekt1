import random
def silnik(): # losowanie przez komputer
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    d = random.randint(1, 9)
    wynik = [a, b, c, d]
    return wynik
def pobierz_liczby(): # pobieranie przez uzytkownika
    inp = []
    for i in range(4):
        a = int(input("Podaj liczbę: "))
        inp.append(a)
    return inp
wylosowane = silnik()
wybor_gracza = pobierz_liczby()

