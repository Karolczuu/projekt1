# projekt python lab3

from silnik import silnik, pobierz_liczby
from checking import checking

def main():
    szukane_cyfry = silnik()
    liczba_rund = 5

    aktualna_runda = 1
    while aktualna_runda <= liczba_rund:
        print("\n===== MASTERMIND =====")
        print("RUNDA NR ", aktualna_runda)

        pobrane_cyfry = pobierz_liczby()

        print("\n\tWYNIKI")
        checking(pobrane_cyfry, szukane_cyfry)

        if pobrane_cyfry == szukane_cyfry:
            print("\n\n=== WYGRAŁEŚ!!! ===")
            print("Liczba rund: ", aktualna_runda)
            return 0
        aktualna_runda += 1

    print("\n\n=== PRZEGRAŁEŚ ===")
    print("Szukane cyfyr to: ")
    print(szukane_cyfry)

main()
