# cosa sono i dict
# come si crea un dict
# len() e type()
# come accedere agli elementi con [], get(), keys(), values(), items()
# verificare se esiste una chiave
# modificare gli elementi con [] e update()
# aggiungere nuovi elementi con [] e update()
# rimuovere gli elementi con pop(key), popitem(), clear(), del
# ciclare gli elementi: key, values, values(), keys(), items()
# copiare dict con copy() e dict()
# dict annidati

# i dictionaries sono collezioni ordinate, modificabili, ma non permettono duplicati (solamente a livello di chiavi)
# a differenza delle altre collezioni di dati, i dict ragionano a coppie di chiavi-valori
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

# len()
print(len(persona))

# type()
print(type(persona))


###########################################################################################################################################
# come accedere ai dati
# come per le tuple e le liste, possiamo usare le parentesi quadre, con la differenza che non dovrò inserire l'indice, ma il nome della chiave da estrarre
# []
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

print(persona["nome"])
###########################################################################################################################################
# .get() - funziona come le quadre, specifico la chiave da estrarre, ed estrarrà il valore corrispondente
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

print(persona.get("nome"))
###########################################################################################################################################
# .keys() - serve per estrarre tutte le chiavi contenute in un dict
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

print(persona.keys())
###########################################################################################################################################
# .values() - serve per estrarre tutti i valori contenuti in un dict
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

print(persona.values())
###########################################################################################################################################
# .items() - serve per estrarre tutte le coppie di chiavi e valori presenti nel dict, sottoforma di lista di tuple
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

print(persona.items())
###########################################################################################################################################
# posso verificare se una chiave esiste
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

print("chiave_particolare" in persona)  #se la chiave è presente il risultato sarà True, altrimenti False


###########################################################################################################################################
# modificare i dati
# posso modificare i dati tramite le parentesi [], specificando al loro interno la chiave il cui valore dovrà essere modificato
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

persona["nome"] = "Giulio"
print(persona)
###########################################################################################################################################
# posso modificare i dati con il metodo .update(), specificando tra le parentesi tonde sia la chiave che il valore da modificare tra parentesi graffe
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

persona.update({"nome": "Federico"})
print(persona)


###########################################################################################################################################
# aggiungere elementi
# posso aggiungere elementi tramite le parentesi [], specificando al loro interno la chiave il cui valore che dovranno essere aggiunti
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

persona["altezza"] = 1.72
print(persona)
###########################################################################################################################################
# posso aggiungere elementi con il metodo .update(), specificando tra le parentesi tonde sia la chiave che il valore da aggiungere tra parentesi graffe
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

persona.update({"altezza": 1.94})
print(persona)


###########################################################################################################################################
# rimuovere elementi
# .pop(key) - posso rimuovere chiave e valore associato specificando la chiave tra le parentesi quadre
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

persona.pop("eta")
print(persona)
###########################################################################################################################################
# .popitem() - rimuoverà l'ultima coppia
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

persona.popitem()
print(persona)
###########################################################################################################################################
# .clear - pulirà tutte le coppie presenti nel dict
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

persona.clear()
print(persona)
###########################################################################################################################################
# del ci permette sia di cancellare una coppia (indicando la coppia tra quadre), che tutto il dict
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

del persona["cognome"]
print(persona)

del persona
# print(persona)


###########################################################################################################################################
# ciclare i dict
# for - con key - estraggo le chiavi
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

for x in persona:
    print(x)
###########################################################################################################################################
# for - con key - estraggo i valori
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

for x in persona:
    print(persona[x])
###########################################################################################################################################
# for - con .values() - estraggo i valori
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

for x in persona.values():
    print(x)                #in questo caso stampo solo x in quanto .values() ci estrae già i valori
###########################################################################################################################################
# for - con .keys() - estraggo le chiavi
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

for x in persona.keys():
    print(x)                #in questo caso stampo solo x in quanto .keys() ci estrae già le chiavi
###########################################################################################################################################
# for - con .items() - estrae le tuple di coppie valori
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

for x, y in persona.items():   # ciclo sia x che y, in quanto attribuisco due variabili ad entrambi i valori presenti all'interno di ogni tupla
    print(x, y)                #in questo caso stampo sia x che y, che riporteranno rispettivamente chiavi e valori



###########################################################################################################################################
# copiare un dict
# .copy() - posso copiare un dict in una seconda variabile
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

x = persona.copy()
print(x)
###########################################################################################################################################
# dict() - costruttore - posso creare un nuovo dict in una seconda variabile
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41
}

x = dict(persona)
print(x)



###########################################################################################################################################
# dict annidati
# posso avere un dict dentro un dict
persona = {
    "nome": "Luca",
    "cognome": "Bianco",
    "eta": 41,
    "indirizzo": {
        "citta": "Milano",
        "indirizzo": "Via Gluck",
        "cap": 20100
    } 
}

print(persona)
# non è un problema estrarre i dati
print(persona["indirizzo"]["citta"])
# proviamo un ciclo - voglio estrarre solo le coppie dell'indirizzo
for i, h in persona["indirizzo"].items():
    print(i, h)