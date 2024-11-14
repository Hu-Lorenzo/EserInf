z=6
spesa = []
def aggiungiElementi():
    n = int(input("Quanti elementi di spesa vuoi inserire "))
    for i in range(n):
        elementi = input("Inserisci un elemento di spesa ")
        spesa.append(elementi)
def stampaElementi():
        print(spesa)
def eliminaElementi():
    stampaElementi()
    n = int(input("Quale elementi di spesa vuoi eliminare "))
    if n == 1 :
        n = 0
    spesa.pop(n)
    stampaElementi()


while z != 0 :
    if z == 1:
        aggiungiElementi()
    if z == 2:
        stampaElementi()
    if z == 3:
        eliminaElementi()
    if z == 0:
        
    


