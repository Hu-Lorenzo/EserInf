
spesa = []
def _aggiungiElementi():
    n = int(input("Quanti elementi di spesa vuoi inserire "))
    for i in range(n):
        elementi = input("Inserisci un elemento di spesa ")
        spesa.append(elementi)
def _stampaElementi():
        print(spesa)
_aggiungiElementi()
_stampaElementi()

