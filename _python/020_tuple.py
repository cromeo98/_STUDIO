# tuple
# le tuple cono collezioni di dati ordinate, indicizzate, non modificabili e che permettono duplicati e di diverso tipo tra di loro
# i vari elementi sono indicati tra parentesi tonde
# creare una tupla normale e con un valore, singole e mischiate
# funzioni len, type e tuple

# accedere agli elementi della lista (singolo, range e negativi)
# verificare se un elemento esiste
# modificare e inserire gli elementi: di base non è possibile, ma esistono dei workaround
# inserire elementi con append(), insert(), extend()
# rimuovere elementi con workaround oppure cancellare tutto con del()
# spacchettare una tupla (unpack) e con *
# ciclare gli elementi
# unire le tuple con join()
# metodi count() e index()

# creiamo una tupla
t = ("Milano", 2, True)
print(t)
# creiamo una tupla con un unico elemento - necessario inserire una virgola dopo il primo elemento, altrimenti risulterebbe essere una stringa
t = ("Milano",)
print(t)

# type - ci mostra il tipo di dato
t = ("Milano",)
print(type(t))

# len - calcola la quantità di elementi all'interno della tupla
t = ("Milano",)
print(len(t))

# tuple - ci permette di creare una tupla
t = tuple(("Milano",))
print(t)
### N.B. se con la funzione tuple() voglio creare una tupla con un solo elemento, devo ricordarmi di inserire la virgola, altrimenti l'elemento verrà considerato una stringa e la tupla avrà tanti elementi quanti sono i caratteri della stringa
t = tuple(("Milano"))
print(t)


###########################################################################################################################################
# le modalità con le quali possiamo accedere agli elementi sono gli stessi delle liste
# per accedere agli elementi, tra parentesi quadre possono spoecificare l'indice che mi interessa estrarre
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(t[2])
# gli indici possono essere utilizzati anche in negativo (parto dall'ultimo elemento e verifico le posizioni a ritroso)
print(t[-2])

# posso anche utilizzare i range tra parentesi quadre, seguendo le regole evidenziate nel file 007, valide anche per le stringhe
# posso estrarre alcuni elementi di una lista
# per farlo posso eseguire il comando: nome_lista[posizione_dalla_quale_partire:posizione_fino_alla_quale_estarre(esclusa)] - t[1:2]
# i due punti vengono utilizzati per separare l'indice dal quale estrarre, all'indice fino al quale si desidera arrivare
# in questo esempio estrarremo "Roma", "Venezia" perchè estrarremo lista[1:3]
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(t[1:3])

# in questo esempio estrarremo "Toronto", "Brasilia" perchè estrarremo lista[3:5], il che significa che partiremo dall'indice 3 e finiremo all'indice 5 (escluso)
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(t[3:5])

# in questo esempio estrarremo "Milano", "Roma", "Venezia" perchè estrarremo lista[:3], il che significa che partiremo dall'indice 0 e finiremo all'indice 3 (escluso)
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(t[:3])

# in questo esempio estrarremo "Venezia", "Toronto", "Brasilia" perchè estrarremo lista[2:], il che significa che partiremo dall'indice 2 e finiremo alla fine della lista
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(t[2:])

# possiamo anche usare gli indici negativi, sia su singolo elemento (partiremo dal fondo) lista[-1]
# che con un range lista[-4:]
# esempio 1: parto dal fondo, e vado indietro di 4 indici (estraggo "Roma", "Venezia", "Toronto", "Brasilia")
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(t[-4:])
# esempio 2: parto dall'inizio, e rispetto al fondo sottraggo all'estrazione 2 indici (estraggo "Milano", "Roma", "Venezia")
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(t[:-2])


###########################################################################################################################################
# verificare se un elemento esiste
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
if "Milano" in t:
    print("OK")


###########################################################################################################################################
# modificare gli elementi delle tuple
# non è possibile modificare gli elementi delle tuple
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
# t[0] = "Parigi" #restituirà l'errore "TypeError: 'tuple" object does not support item assignment

# workaround
# prendere la tupla e assegnarla ad una lista, modificare la lista, assegnare i valori della lista alla tupla
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(t)
l = list(t)
l[0] = "Parigi"
t = tuple(l)
print(t)
# lo stesso workaround è utilizzabile con remove, pop, append, insert, extend
# del ci permette di cancellare l'elemento


###########################################################################################################################################
# unpack delle tuple
# unpack significa spezzettare in diverse variabili gli elementi delle tuple
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
(a, b, c, d, e) = t
print(a, b, c, d, e)
# nel caso in cui la tupla avesse più valori rispetto alle variabili indicate posso inserire un asterisco prima dell'ultima variabile
# ciò comporterà la creazione di una lista sull'ultima variabile
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
(a, b, c, *d) = t
print(a, b, c, d)

###########################################################################################################################################
# ciclare gli elementi - funziona esattamente come per le liste
# for
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
for i in range(len(t)):
    print(t[i])

#while
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
i = 0
while i < len(t):
    print(t[i])
    i += 1


###########################################################################################################################################
# unire due tuple - necessario creare una nuova variabile
t1 = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
t2 = tuple(("Parigi",))

t = t1 + t2
print(t)


###########################################################################################################################################
# metodi count() e index()
# count ci permette di conteggiare quante volte un valore è ripetuto al'interno di una tupla
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia", "Milano"))
x = t.count("Milano")
print(x)

# index ci permette di verificare l'indice di un valore - solamente la prima ricorrenza nel caso di valori duplicati
t = tuple(("Milano", "Roma", "Venezia", "Toronto", "Brasilia", "Milano"))
x = t.index("Milano")
print(x)

