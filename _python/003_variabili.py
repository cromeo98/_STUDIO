# 1 - cos'è una variabile
# 2 - nomenclatura
# 3 - assegnare multipli valori
# 4 - utilizzare una variabile
# 5 - collection


# 1
# La variabile è un contenitore di dati


# 2 
# su python le variabili non sono "dichiarabili"
# devo necessariamente assegnare ad una variabile un valore
# in questo caso "x" è stata creata correttamente, "y" no
# ---- x = 5
# ---- y
# y riporterà da terminale "NameError: name "y" is not defined



# 3
# i nomi delle variabili sono case sensitive
# sono disponibili numeri, caratteri alfabetici e underscore "_"
# tipologia di case:
# - camelCase
# - PascalCase
# - snake_case
# da documentazione ufficiale il consiglio è quello di usare lo snake_case

# i caratteri illegali sono:
# - le varibaili non possono iniziare con un numero
# - non possono esserci spazi
# - non possono esserci meno "-"


# 4 
# per assegnare più valori contemporaneamente, possiamo definire più variabile contemporaneamente separate da virgola
# dopo l'uguale "=", posso inserire più valori separati da virgola
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
# se invece tutte le variabili devono avere lo stesso valore, devo sostituire alle virgole l'uguale "="
x = y = z = 32
print(x)
print(y)
print(z)
# posso anche stampare a schermo tutte le variabili insieme, inserendole separate da virgola all'interno delle parentesi del print
print(x, y, z)

# posso svolgere operazioni matematiche tra le varibili
x = 1
y = 5
z = x*y + y
print(z)


# 5
# cos'è una collection?
# una collection è una lista di dati contenuti all'interno di una variabile
# i dati sono assegnati dopo l'uguale "=" e sono compresi tra parentesi quadra
citta = ["roma", "milano", "napoli"]
# cos'è un unpack?
# l'unpack è letteralmente uno "spacchettamento" di dati contenuti all'interno di una collection
# posso quindi assegnare ad una o più variabili i valori contenuti all'interno di una collection
x, y, z = citta
print(x, y, z)
# se però, le variabili messe in relazione con la collection sono inferiori rispetto ai dati inseriti all'interno della collection
# x, y = citta
# avremo un errore: ValueError: too many values to unpack

