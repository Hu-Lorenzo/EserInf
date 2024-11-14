z=6
spesa = []
def _aggiungiElementi():
    n = int(input("Quanti elementi di spesa vuoi inserire "))
    for i in range(n):
        elementi = input("Inserisci un elemento di spesa ")
        spesa.append(elementi)
def _stampaElementi():
        print(spesa)
def _eliminaElementi():
    _stampaElementi()
    n = int(input("Quale elementi di spesa vuoi eliminare "))
    if n == 1 :
        n = 0
    spesa.pop(n)
    _stampaElementi()

def _termina():
    break



while z != 0 :
     if z == 1:
        _aggiungiElementi()
     if z == 2:
        __stampaElementi()
     if z == 3:
        _eliminaElementi()
     if z == 0:
        _termina()
    


