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
def contaElementi():
        print(len(spesa))
def svotaElementi():
        spesa.clear()
        print("Lista svotata")


while z != 0 :
    print("N'0 Esci dal comando")
    print("N'1 comando per aggiungere elemento")
    print("N'2 comando per stampare elemento")
    print("N'3 comando per eliminare elemento")
    print("N'4 comando per contare elemento")
    print("N'5 comando per svotare elemento")
    z = int(input("Seleziona numero di comando: "))
    if z == 1:
        aggiungiElementi()
    if z == 2:
        stampaElementi()
    if z == 3:
        eliminaElementi()
    if z == 4:
        contaElementi()
    if z == 5:
        svotaElementi()
    if z == 0:
       break 
    


