# sintassi
# utilizzo con stringhe, liste, range
# break, continue, else

# il for è un ciclo che ci permette di reiterare una sequenza (non viene utilizzata una condizione)

#es. con lista
lista_citta = ["milano", "roma", "napoli"]
for x in lista_citta:   #per ogni elemento presente nella collezione
    print(x, end=" ")   #eseguo

#es. con stringa
stringa = "ciao"
for letter in stringa:
    print(letter)

#es. con range
for n in range(1,5):
    print(n)
else:
    print("Ho finito")

#i costrutti break, continue ed else sono identici a quelli del while
#anche con il ciclo for possiamo innestare gli IF
# i cicli for sono molto utili con le tabelle:
for riga in range(5):
    for colonna in range(5):
        print("(", riga, ":", colonna, ")")