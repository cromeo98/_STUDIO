# come creare una lista
# len, type, list()
# come accedere gli elementi
# come modificare gli elementi 
# inserire nuovi elementi con append(), insert(), extend()
# rimuovere gli elementi con remove(), pop(), del(), clear()
# ciclare gli elementi
# list comprehension
# modificare l'ordine
# copiare una list con copy()
# unire più liste assieme con +, append(), extend()

# innanzitutto, ricordiamo la definizione di lista:
# è una collezione ordinata, indicizzata, modificabile e che permette duplicati
# n.b. non ci sono limiti alle tipologie di elementi che possono essere inseriti all'interno della lista

# come creiamo una lista?
# 1 - dichiarazione della variabile come lista
x = ["milano", 13, True, "nathan"]
# 2 - costruttore list()
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))

# funzione type() - ci permette di estrarre l'informazione relativa alla tipologia della variabile, in questo caso 'list'
print(type(x))
# funzione len() - ci permette di estrarre la lunghezza (in numero) della lista (numero di elementi contenuti al suo interno)
print(len(x))

###########################################################################################################################################
# per accedere agli elementi, tra parentesi quadre possono spoecificare l'indice che mi interessa estrarre
print(x[2])
# gli indici possono essere utilizzati anche in negativo (parto dall'ultimo elemento e verifico le posizioni a ritroso)
print(x[-2])

# posso anche utilizzare i range tra parentesi quadre, seguendo le regole evidenziate nel file 007, valide anche per le stringhe
# posso estrarre alcuni elementi di una lista
# per farlo posso eseguire il comando: nome_lista[posizione_dalla_quale_partire:posizione_fino_alla_quale_estarre(esclusa)] - x[1:2]
# i due punti vengono utilizzati per separare l'indice dal quale estrarre, all'indice fino al quale si desidera arrivare
# in questo esempio estrarremo "Roma", "Venezia" perchè estrarremo lista[1:3]
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(x[1:3])

# in questo esempio estrarremo "Toronto", "Brasilia" perchè estrarremo lista[3:5], il che significa che partiremo dall'indice 3 e finiremo all'indice 5 (escluso)
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(x[3:5])

# in questo esempio estrarremo "Milano", "Roma", "Venezia" perchè estrarremo lista[:3], il che significa che partiremo dall'indice 0 e finiremo all'indice 3 (escluso)
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(x[:3])

# in questo esempio estrarremo "Venezia", "Toronto", "Brasilia" perchè estrarremo lista[2:], il che significa che partiremo dall'indice 2 e finiremo alla fine della lista
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(x[2:])

# possiamo anche usare gli indici negativi, sia su singolo elemento (partiremo dal fondo) lista[-1]
# che con un range lista[-4:]
# esempio 1: parto dal fondo, e vado indietro di 4 indici (estraggo "Roma", "Venezia", "Toronto", "Brasilia")
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(x[-4:])
# esempio 2: parto dall'inizio, e rispetto al fondo sottraggo all'estrazione 2 indici (estraggo "Milano", "Roma", "Venezia")
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
print(x[:-2])

###########################################################################################################################################
# modificare gli elementi
# singolo elemento list[i] = "abcde"
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
x[0] = "Parigi"
print(x)

# elementi in range list[i:i] = ["abcde","fghil"] - anche in questo caso è valida l'esclusione dell'indice finale
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
x[0:2] = ["Parigi", "Cartagena"]
print(x)
# se con il range andassi a riassegnare solo un elemento ad una selezione di più elementi, questi verrebbero rimossi, e rimarrebbe solamente il nuovo elemento
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
x[0:3] = ["Parigi"]
print(x)

# metodo .append(), va ad aggiungere in fondo alla lista il valore indicato tra parentesi
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
x.append("Parigi")
print(x)

# metodo .insert(), posso specificare qual è la posizione entro la quale aggiungere il valore; l'indicazione della posizione serve come parametro di inserimento, non modifica, quindi l'elemento già presente in quella posizione non verrà modificato/eliminato, ma spostato di posizione in avanti
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
x.insert(1, "Parigi")
print(x)

# metodo .extend(), posso unire due liste
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
y = ["Ciao", "Hello"]
x.extend(y)
print(x)


###########################################################################################################################################
# rimuovere elementi da una lista
# metodo remove() - posso specificare l'elemento da cancellare
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
x.remove("Milano")
print(x)

# metodo pop() - posso specificare l'indice da cancellare (altrimenti verrà cancellato l'ultimo indice)
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
x.pop(1)
print(x)

# del - permette di cancellare o un indice specifico o la variabile nella sua totalità
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
del x[0]
print(x)

# del x
# print(x)    # restituisce errore in quanto x non esiste più

# metodo clear - permette di pulire i dati contenuti all'interno della lista senza cancellarla
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
x.clear()
print(x)


###########################################################################################################################################
# ciclare gli elementi
x = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))
for citta in x:
    print(citta)

# usare gli indici
for i in range(len(x)):
    print(x[i])

# usare il while
i = 0
while i < len(x):
    print(x[i])
    i += 1

# list comprehension ci da la possibilità di usare una sintassi ridotta
lista_citta = list(("Milano", "Roma", "Venezia", "Toronto", "Brasilia"))

[print(citta) for citta in lista_citta] #[espressione da eseguire per ogni elemento in lista/range condizione]
# [espressione for item in list if condition == True]

#con la list comprehension abbiamo la possibilità di creare facilmente una nuova lista
y = [citta for citta in lista_citta if citta != "Roma"]
print(y)


###########################################################################################################################################
# modificare l'ordine di una lista
# metodo sort() - ordina in maniera crescente (o alfabetico o numerico) la nostra lista
x =[1, 150, 26, 50, 87]
x.sort()
print(x)

# posso anche ordinare decrescentemente indicando all'interno delle parentesi reverse=True
x =[1, 150, 26, 50, 87]
x.sort(reverse=True)
print(x)

###########################################################################################################################################
# copy di una list
# fare attenzione ad una cosa: se per "copiare una lista" la dichiaro all'interno di un'altra variabile, questa non risulta essere una vera copia, ma soltanto un riferimento
# ciò significa che nel momento in cui modifico i valori di una delle due variabili, ne sarà influenzata anche la seconda:
x = ["a", "b", "c", "d"]
y = x
y[0] = "z"
print(x)    # nonostante abbia modificato solamente y, la modifica è visibile all'interno di x
# per copiare realmente quindi dobbiamo usare il metodo .copy()
x = ["a", "b", "c", "d"]
y = x.copy()
y[0] = "z"
print(x)
#### oppure
# possiamo usare il costruttore list
x = ["a", "b", "c", "d"]
y = list(x)
y[0] = "z"
print(x)
print(y)


###########################################################################################################################################
# unire più liste assieme (+, append(), extend())
x = ["Bari nuova", "Bari vecchia"]
y = ["Bergamo alta", "Bergamo bassa"]

# +
x = ["Bari nuova", "Bari vecchia"]
y = ["Bergamo alta", "Bergamo bassa"]
z = x + y
print(z)

# append - richiede un ciclo for
x = ["Bari nuova", "Bari vecchia"]
y = ["Bergamo alta", "Bergamo bassa"]
for citta in y:
    x.append(citta)
print(x)
# il metodo append, senza ciclo, tra due liste, crea una lista innestata
x = ["Bari nuova", "Bari vecchia"]
y = ["Bergamo alta", "Bergamo bassa"]
x.append(y)
print(x)

#extend
x = ["Bari nuova", "Bari vecchia"]
y = ["Bergamo alta", "Bergamo bassa"]
x.extend(y)
print(x)