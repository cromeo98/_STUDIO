# Liste
# Esercizio 1
# Creare una lista vuota e assegnarla a una variabile.
lst = []

# Esercizio 2
# Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile.
lst = list((1, 2, 3, 4, 5))

# Esercizio 3
# Accedere all'elemento con indice 2 della lista precedente.
#print(lst[2])

# Esercizio 4
# Aggiungere un nuovo elemento "6" alla lista precedente
#lst.append(6)         #il nuovo elemento andrà in fondo
# or
#lst.insert(5, 6)      #specifico l'indice nel quale verrà inserito in nuovo elemento
#print(lst)

# Esercizio 5
# Rimuovere l'elemento con indice 3 dalla lista precedente.
#lst.pop(3)
#print(lst)

# Esercizio 6
# Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.
#lst_2 = list(lst[:3])
#print(lst_2)

# Esercizio 7
# Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.
#lst_2 = []
#
#for i in lst:
#    if (i - 1) % 2 != 0:
#        lst_2.append(lst[(i - 1)])
#
#print(lst_2)

# Esercizio 8
# Ordinare la lista precedente in ordine decrescente.
# lst.sort(reverse=True)
# print(lst)

# Esercizio 9
# Contare quante volte l'elemento "2" appare nella lista precedente.
# n = lst.count(2)
# print(n)

###########################################################################################################################################
# Tuple
# Esercizio 1
# Creare una tupla vuota e assegnarla a una variabile.
tup = tuple(())
# or
# tup = ()
# print(type(tup))

# Esercizio 2
# Creare una tupla con i seguenti elementi: "mela", "banana", "kiwi".
tup = ("mela", "banana", "kiwi")
# print(tup)

# Esercizio 3
# Accedere all'elemento "banana" della tupla precedente.
# print(tup[1])

# Esercizio 4
# Creare una nuova tupla che contenga solo i primi due elementi della tupla precedente.
tup_2 = tuple(tup[:2])
# print(tup_2)

# Esercizio 5
# Verificare se l'elemento "ananas" è presente nella tupla precedente.
# print("ananas" in tup_2)

# Esercizio 6
# Creare una nuova tupla concatenando la tupla precedente con la tupla ("pesca", "arancia").
tup_3 = ("pesca", "arancia")

tup_4 = tup_2 + tup_3
# print(tup_4)

# Esercizio 7
# Verificare la lunghezza della tupla precedente.
# print(len(tup_4))

# Esercizio 8
# Creare una tupla contenente i numeri interi da 1 a 5.
tup_5 = (1, 2, 3, 4, 5)
# print(type(tup_5))

# Esercizio 9 (difficile)
# Creare una tupla contenente il quadrato dei numeri interi da 1 a 5.
# lst = []
# for i in range(1, 6):
#     lst.append(i**2)

#print(lst)

# tup = tuple(lst)
# print(tup)

# Esercizio 10
# Contare il numero di occorrenze dell'elemento "mela" nella tupla precedente.
#print(tup_4.count("mela"))

###########################################################################################################################################
# Dict
# Esercizio 1
# Creare un dizionario vuoto e assegnarlo a una variabile.
dict = {}
# print(type(dict))

# Esercizio 2
# Creare un dizionario con le seguenti chiavi e valori: "nome" : "Mario", "cognome" : "Rossi", "età" : 30.
person = {
    "nome" : "Mario",
    "cognome" : "Rossi",
    "età" : 30
}

# print(person)

# Esercizio 3
# Accedere al valore dell'elemento con chiave "età" del dizionario precedente.
person = {
    "nome" : "Mario",
    "cognome" : "Rossi",
    "eta" : 30
}

# print(person["eta"])

# Esercizio 4
# Aggiungere un nuovo elemento "email" con valore "mario.rossi@email.com" al dizionario precedente.
person["email"] = "mario.rossi@email.com"
# or
# person.update({"email" : "mario.rossi@email.com"})

# print(person)

# Esercizio 5
# Rimuovere l'elemento con chiave "cognome" dal dizionario precedente.
del person["cognome"]
# or
# person.pop("cognome")

# print(person)

# Esercizio 6
# Creare una nuova lista che contenga solo le chiavi del dizionario precedente.
keys = list(person.keys())

# print(keys)

# Esercizio 7
# Creare una nuova lista che contenga solo i valori del dizionario precedente.
values = list(person.values())

# print(values)

# Esercizio 8
# Aggiornare il valore dell'elemento con chiave "età" del dizionario precedente a 35.
person["eta"] = 35
# or
# person.update({"eta": 35})

# (person["eta"])

# Esercizio 9
# Contare il numero di elementi nel dizionario precedente.
counter = 0
for i in person.items():
    counter += 1
# print(counter)
# or
# print(len(person))


###########################################################################################################################################
# Set
# Esercizio 1
# Creare un set vuoto e assegnarlo a una variabile.
m_set = set()
# print(type(m_set))

# Esercizio 2
# Creare un set contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".
fruits = {"mela", "banana", "kiwi", "mela"}
# print(fruits)

# Esercizio 3
# Aggiungere l'elemento "pesca" al set precedente.
fruits.update({"pesca"})
# print(fruits)

# Esercizio 4
# Rimuovere l'elemento "mela" dal set precedente.
fruits.remove("mela")
# print(fruits)

# Esercizio 5
# Verificare se l'elemento "ananas" è presente nel set precedente.
# print("banana" in fruits)

# Esercizio 6
# Creare un nuovo set contenente gli elementi "banana", "kiwi" e "arancia".
tropical_fruits = set(("banana", "kiwi", "arancia"))
# print(tropical_fruits)

# Esercizio 7
# Creare un set contenente i numeri interi da 1 a 5 ricavati da un range().
num_set = set()
for i in range(1,6):
    num_set.update({i})

# or 
# num_set = set(range(1,6))

#print(num_set)

# Esercizio 8 (difficile)
# Creare un nuovo set contenente i numeri pari del set precedente.
p_num_set = set()

for i in num_set:
    if not (i % 2):
        p_num_set.add(i)

# or
# p_num_set = set(x for x in num_set if x % 2 ==0)

print(p_num_set)