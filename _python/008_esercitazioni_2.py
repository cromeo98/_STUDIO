# Esercizio 1
# Assegnare una stringa "ciao mondo" ad una variabile "stringa" e utilizzare il metodo upper() per convertirla in maiuscolo in una nuova variabile.
stringa = "ciao mondo"
stringa_maiusc = stringa.upper()
print(stringa_maiusc)
# Esercizio 2
# Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" e utilizzare il metodo lower() per convertirla in minuscolo in una nuova variabile.
stringa = "Benvenuti a Roma"
stringa_minus = stringa.lower()
print(stringa_minus)
# Esercizio 3
# Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" e utilizzare il metodo split() per dividere la stringa in una lista di parole.
stringa = "Il meglio deve ancora venire"
stringa_splitted = stringa.split()
print(stringa_splitted)
# Esercizio 4
# Assegnare una stringa "Hello World" ad una variabile "stringa" e utilizzare il metodo replace() per sostituire "World" con "Python".
stringa = "Hello World"
stringa_replaced = stringa.replace("World", "Python")
print(stringa_replaced)
# Esercizio 5
# Assegnare una stringa " Ciao " ad una variabile "stringa" e utilizzare il metodo strip() per rimuovere gli spazi vuoti all'inizio e alla fine della stringa..
stringa = "  Ciao  "
stringa_stripped = stringa.strip()
print(stringa_stripped)
# Esercizio 6
# Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.
stringa = "abcdefg"
stringa_primi_tre_chr = stringa[:3]
print(stringa_primi_tre_chr)
# Esercizio 7
# Assegnare una stringa "Python" ad una variabile "stringa" e utilizzare il metodo startswith() per verificare se la stringa inizia con "Py".
stringa = "Python"
print(stringa.startswith("Py")) #risultato true
# Esercizio 8
# Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e utilizzare il metodo count() per contare il numero di volte in cui la lettera "o" appare nella stringa.
stringa = "Ciao Mondo"
print(stringa.count("o"))
# Esercizio 9
# Assegnare una stringa "Ciao mondo" ad una variabile "stringa". Mandare quindi a schermo gli ultimi 5 caratteri della stringa in maiuscolo, sostituendo il carattere "o" con "k".
stringa = "Ciao Mondo"
stringa_last_five_chr = stringa[-5:]
print(stringa_last_five_chr)
stringa_maiusc = stringa_last_five_chr.upper()
print(stringa_maiusc)
stringa_replaced = stringa_maiusc.replace("O", "K")
print(stringa_replaced)
#### OPPURE
stringa = "Ciao Mondo"
print(stringa.replace("o", "k").upper()[-5:])
#ciao