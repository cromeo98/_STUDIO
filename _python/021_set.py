# cosa sono i set
# come si crea un set, normale e mischiato
# len, type, set()
# come accedere agli elementi del set
# come modificare gli elementi (non è possibile modificarli, solo aggiungerne o rimuoverne)
# come aggiungere gli elementi  con add() e update()
# come rimuovere gli elementi con remove(), discard(), pop(), clear() e del
# unire i set con union() e update(), intersction_update(), intersection(), symmetric_diference_update(), symmetric_difference()

# i set sono delle collezioni non ordinate, di conseguenza non indicizzate, non modificabili e che non permettono valori duplicati
# questo li porta ad essere le collezioni più statiche di python

# creiamo un set - la sintassi è tra parentesi graffe
x = {"milano", "roma", "napoli"}
y = {"milano", 26, True}

# vediamo le funzioni:
# len()
x = {"milano", "roma", "napoli"}
print(len(x))
# type()
x = {"milano", "roma", "napoli"}
print(type(x))
# set() - costruttore, mi permette di creare i set
x = set(("milano", "roma", "napoli"))
print(x)

# accedere ai dati
# non essendo una collezione indicizzata, l'unico modo per accedere ai dati è tramite un loop
# il loop, restituirà i dati sempre in maniera randomica
x = set(("milano", "roma", "napoli"))
for i in x:
    print(i)

# possiamo comunque eseguire il nostro check di verifica se un elemento esiste
x = set(("milano", "roma", "napoli"))
print("milano" in x)


###########################################################################################################################################
# non possiamo modificare i dati, ma possiamo aggiungerne o rimuoverne
# add 
x = set(("milano", "roma", "napoli"))
x.add("Parigi")
print(x)
# update - ci permette di unire un set ad un altro (funziona anche con le liste e con le tuple)
x = set(("milano", "roma", "napoli"))
y = {"Parigi", "Londra"}
x.update(y)
print(x)

###########################################################################################################################################
# rimuovere gli elementi
# i metodi .remove() e .discard() vanno di pari passo, è necessario specificare tra parentesi qual è l'elemento che deve essere rimosso
# la differenza è che se provo a rimuovere un elemento che non è presente nel set con .remove(), mi verrà riportato un errore
# mentre se provo a farlo con .discard() non succederà nulla
# remove
x = set(("milano", "roma", "napoli"))
x.remove("milano")
print(x)
# discard
x = set(("milano", "roma", "napoli"))
x.discard("roma")
print(x)

# pop - rimuove l'ultimo elemento, ma non essendo gli elementi dei set indicizzati, la rimozione sarà casuale
x = set(("milano", "roma", "napoli"))
x.pop()
print(x)

# clear - rende il set vuoto
x = set(("milano", "roma", "napoli"))
x.clear()
print(x)

# del - cancella la variabile
x = set(("milano", "roma", "napoli"))
del x
#print(x)


###########################################################################################################################################
# unire più set
# .union() - creerà un nuovo set
x = set(("milano", "roma", "napoli"))
y = {"Parigi", "Londra"}

z = x.union(y)
print(z)

# .update() - non è necessario creare un nuovo set
x = set(("milano", "roma", "napoli"))
y = {"Parigi", "Londra", "roma"}

x.update(y)
print(x)
# n.b. nè .update() nè .union() duplicherranno i dati se presenti nei set coinvolti


###########################################################################################################################################
# .intersection() - serve per estrarre solamente i valori presenti in entrambi i set, necessita di una nuova variabile
x = set(("milano", "roma", "napoli"))
y = {"Parigi", "Londra", "roma"}

z = x.intersection(y)
print(z)

# .intersection_update() - serve per estrarre solamente i valori presenti in entrambi i set, NON necessita di una nuova variabile
x = set(("milano", "roma", "napoli"))
y = {"Parigi", "Londra", "roma"}

x.intersection_update(y)
print(x)


###########################################################################################################################################
# .symmetric_difference() - serve per estrarre solamente i valori diversi tra i set, necessita di una nuova variabile
x = set(("milano", "roma", "napoli"))
y = {"Parigi", "Londra", "roma"}

z = x.symmetric_difference(y)
print(z)

# .symmetric_difference_update() - serve per estrarre solamente i valori diversi tra i set, NON necessita di una nuova variabile
x = set(("milano", "roma", "napoli"))
y = {"Parigi", "Londra", "roma"}

x.symmetric_difference_update(y)
print(x)