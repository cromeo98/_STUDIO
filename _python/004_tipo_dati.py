# 1 - ottenere il tipo di dato di una variabile
# 2 - come assegnare un tipo di dato
# 3 - tipi di dati

# 1 
# per ottenere il tipo di dato esiste la funzione "type"
x = 5.5
type(x)
# type da solo però non fornisce alcun output, quindi per avere evidenza del tipo di dato è necessario combinarlo con il print
print(type(x))
# il risultato da terminale è <class 'float'>

# 2
# python assegna automaticamente il tipo valore ad una variabile
# per questo motivo posso assegnare tipi di dati diversi ad una variabile indipendentemente dal suo tipo di dato precedente
x = "ciao"
print(type(x))
# il risultato da terminale è <class 'str'>

# 3
# ecco alcuni tipi di dati:
# stringa
# str: x = "ciao"
x = "ciao"
print(type(x))

# numero intero
# int: x = 2
x = 2
print(type(x))

# numero decimale, i decimali sono espressi coni l punto "."
# float: x = 2.5
x = 2.5
print(type(x))

# booleano, attenzione, la condizione True o False deve avere l'iniziale maiuscola
# bool: x = True
x = True
print(type(x))

# lista (collezione), tra parentesi quadre - non confondere con gli array
# list: x = ["milano", "roma", "napoli"]
x = ["milano", "roma", "napoli"]
print(type(x))

# tupla (collezione), tra parentesi tonde
# tuple: x = ("milano", "roma", "napoli")
x = ("milano", "roma", "napoli")
print(type(x))

# range, generatore di valori
# range: x = range(6)       # corrisponde ad una list: x = [0, 1, 2, 3, 4, 5]
x = range(6)
print(type(x))

# dizionario, ad ogni chiave corrisponde un valore, tra parentesi graffe e con separazione tra chiavi e valori con due punti ":"
# dict: x = {"nome": "Christian", "eta": 25}
x = {"nome": "Christian", "eta": 25}
print(type(x))

# set, valori separati da parentesi graffe
# set: x = {"milano", "roma", "napoli"}
x = {"milano", "roma", "napoli"}
print(type(x))

