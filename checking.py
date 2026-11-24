#A - wylosowana lista
#B - lista użytkownika
def checking(A, B):

    #deklarowanie kolorów do printowania
    RESET = '\033[0m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

    #resetowanie koloru
    print(RESET) 

    for i in range(len(A)):
        if B[i] == A[i]: #Dobre mejsce na liście
            print(GREEN, A[i], RESET, end=" ")
        elif B[i] in A and B[i] != A[i]: #Złe miejsce ale liczba istnieje w liście
            print(YELLOW, A[i], RESET, end=" ")
        else:       #Złe wszystko
           print(RED, A[i], RESET, end=" ")
