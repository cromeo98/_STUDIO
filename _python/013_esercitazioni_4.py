# Esercizio 1
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è positivo" se il numero è maggiore di zero, altrimenti stampa "Il numero è negativo".
# numero_utente = int(input("Inserisci un numero"))
# if numero_utente >= 0:
#     print("numero scelto maggiore o uguale a 0")
# else:
#     print("numero scelto minore di 0")

# Esercizio 2
# Scrivere un programma che chiede all'utente di inserire due numeri e stampa "Il primo numero è maggiore" se il primo numero è maggiore del secondo, "Il secondo numero è maggiore" se il secondo numero è maggiore del primo, altrimenti stampa "I numeri sono uguali".
# numero_1 = int(input("Inserisci il primo numero: "))
# numero_2 = int(input("Inserisci il secondo numero: "))
# if numero_1 > numero_2:
#     print("Il primo numero è maggiore")
# elif numero_1 < numero_2:
#     print("Il primo numero è minore")
# else:
#     print("I numeri sono uguali")

# Esercizio 3
# Scrivere un programma che chiede all'utente di inserire una stringa e stampa "La stringa è vuota" se la stringa è vuota, altrimenti stampa "La stringa non è vuota".
# stringa = input("Inserisci una frase o una parola o un carattere")
# if stringa:
#     print("La stringa è stata inserita correttamente")
# else:
#     print("La stringa è vuota")

# Esercizio 4
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è pari" se il numero è pari, altrimenti stampa "Il numero è dispari".
# numero_utente = int(input("Inserisci un numero"))
# if numero_utente % 2 == 0:
#     print("Il numero è pari")
# else:
#     print("Il numero è dispari")

# Esercizio 5
# Scrivere un programma che chiede all'utente di inserire una lettera e stampa "La lettera è una vocale" se la lettera è una vocale (a, e, i, o, u), altrimenti stampa "La lettera non è una vocale".
# lettera_utente = input("Inserisci una lettera: ")
# vocali = ("a", "e", "i", "o", "u")
# if lettera_utente in vocali:
#     print("la lettera è una vocale")
# else:
#     print("la lettera è una consonante")
# ##### oppure
# lettera_utente = input("Inserisci una lettera: ")
# vocali = "aeiou"
# if lettera_utente in vocali:
#     print("la lettera è una vocale")
# else:
#     print("la lettera è una consonante")

# Esercizio 6
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è compreso tra 1 e 10" se il numero è compreso tra 1 e 10, altrimenti stampa "Il numero non è compreso tra 1 e 10".
# numero_utente = int(input("Inserisci un numero: "))
# if numero_utente >= 1:
#     if numero_utente < 11:
#         print("Il numero è compreso tra 1 e 10")
#     else:
#         print("Il numero non è compreso tra 1 e 10")
# else:
#     print("Il numero non è compreso tra 1 e 10")
    
# ##### Oppure

# if 1 <= numero_utente <= 10:
#     print("Il numero è compreso tra 1 e 10")
# else:
#     print("Il numero non è compreso tra 1 e 10")

# ##### Oppure

# if numero_utente >= 1 and numero_utente <= 10:
#     print("Il numero è compreso tra 1 e 10")
# else:
#     print("Il numero non è compreso tra 1 e 10")

# Esercizio 7
# Scrivere un programma che chieda all'utente di inserire un numero intero. Se il numero è maggiore di 10, stampare "Il numero è maggiore di 10". Se il numero è uguale a 10, stampare "Il numero è uguale a 10". Se il numero è minore di 10, stampare "Il numero è minore di 10".
# numero_utente = int(input("Inserisci un numero: "))
# if numero_utente > 10:
#     print("Il numero è maggiore di 10")
# elif numero_utente < 10:
#     print("Il numero è minore di 10")
# else:
#     print("Il numero è uguale a 10")

# Esercizio 8
# Scrivere un programma che chieda all'utente di inserire un carattere. Se il carattere è una vocale (a, e, i, o, u) con isalpha(), stampare "Il carattere inserito è una vocale". Se il carattere è una consonante, stampare "Il carattere inserito è una consonante". Se il carattere non è una lettera, stampare "Il carattere inserito non è una lettera".
# lettera_utente = input("Inserisci una lettera: ")
# if not(lettera_utente.isalpha()):
#     print("Attenzione! non hai inserito una lettera")
# else:
#     if lettera_utente in "aeiou":
#         print("la lettera è una vocale") 
#     else:
#         print("la lettera è una consonante")

# Esercizio 9 (difficile)
# Scrivi un programma che chieda all'utente di inserire tre numeri interi che rappresentano i lati di un triangolo. Il programma deve verificare se questi tre numeri formano un triangolo rettangolo. Se i tre numeri soddisfano la condizione per essere un triangolo rettangolo (cioè rispettano il teorema di Pitagora), allora stampa "I tre numeri formano un triangolo rettangolo". Altrimenti, stampa "I tre numeri non formano un triangolo rettangolo".
a = int(input("Inserisci l\'ipotenusa del rettangolo: ")) 
b = int(input("Inserisci il primo cateto del rettangolo: "))
c = int(input("Inserisci il secondo cateto del rettangolo: "))

if a ** 2 == b ** 2 + c ** 2:
    print("I tre numeri formano un triangolo rettangolo")
else: 
    print("I tre numeri non formano un triangolo rettangolo")