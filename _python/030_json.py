# utilissimo per il collegamento con il front end (comunicazione con .js asincrono con ajax)
# come leggere il json in json
# come convertire da python in json per esportare i dati
# dati convertibili in json (in python)
    # dict (dizionari): In JSON corrispondono agli oggetti.
    # Python: {"chiave": "valore"} → JSON: {"chiave": "valore"} 
# 
    # list (liste): In JSON corrispondono agli array.
    # Python: ["uno", "due", "tre"] → JSON: ["uno", "due", "tre"]   
# 
    # tuple (tuple): In JSON vengono convertite in array, come le liste.
    # Python: ("uno", "due") → JSON: ["uno", "due"] 
# 
    # str (stringhe): Corrispondono alle stringhe in JSON.
    # Python: "testo" → JSON: "testo"   
# 
    # int (interi): Corrispondono ai numeri in JSON.
    # Python: 42 → JSON: 42 
# 
    # float (numeri decimali): Corrispondono ai numeri in JSON.
    # Python: 3.14 → JSON: 3.14 
# 
    # bool (booleani): Corrispondono ai valori booleani in JSON (true e false).
    # Python: True → JSON: true, False → JSON: false    
# 
    # None: Corrisponde a null in JSON.
    # Python: None → JSON: null
# come formattare il json
# ordinare il json

# è necessario importare il modulo JSON
import json

# i json arrivano come stringa
x = '{ "nome": "Luca", "cognome": "Rossi", "eta": 25}'

# in python vengono trasformati in dict; per farlo dobbiamo usare il metodo .loads() 
y = json.loads(x)

# print(y)
# print(type(y))

# possiamo quindi chiamare y proprio come fosse un normalissimo dict
# print(y["nome"])

# come faccio a trasformare i dict di python in un formato json?
# creiamo il nostro dict
x = { 
    "nome": "Luca", 
    "cognome": "Rossi", 
    "eta": 25
}

# per farlo dobbiamo utilizzare il metodo json.dumps()
y = json.dumps(x)

# print(y)
# print(type(y)) #è una stringa

# posso passare al formato json tutti i tipi di dati sopra riportati

# formattazione e ordinamento del json
# ampliamo il nostro dict
x = { 
    "nome": "Luca", 
    "cognome": "Rossi", 
    "eta": 25,
    "altezza": 172,
    "residenza": {
        "indirizzo": "Via Roma",
        "civico": "27",
        "cap": "20156",
        "citta": "Milano",
        "provincia": "MI",
        "stato": "IT"
    },
    "interessi": ["calcio", "cucina", "back-end"]
}

# la formattazione e l'ordinamento ci permettono di rendere più leggibile il json
# la formattazione avviene nel metodo dumps, con l'attributo indent, che ci permette di attribuire un'indentazione al json
# y = json.dumps(x, indent=2)
# print(y)

# con l'attributo separators definiamo quali dovranno essere i separatori tra un elemento e il successivo (di default ", ") e tra le coppie chiave valore (di default ": "), scrivendolo possiamo modificare i separatori
# nell'esempio sotto riportato, sostituiamo ", " e ": " con "| " e "= "
# y = json.dumps(x, indent=2, separators=("| ", "= "))
# print(y)

# abbiamo anche la possibilità di ordinare le chiavi
# per farlo, nel dumps possiamo indicare l'attributo sort_keys=True, le chiavi verranno ordinate in ordine alfabetico
y = json.dumps(x, indent=2, sort_keys=True)
print(y)