# - if
# - operatori di comparazione
# - elif e else
# - operatori logici: and e or
# - versione short hand
# - if innestati

# gli if servono a definire delle condizioni e conseguentemente definire gli script da eseguire quando la condizione è rispettata o no
# come si scrive:
# if condizione:
#       script da eseguire (fondamentale l'indentazione)
if 11 > 10:
    print("condizione vera!")
# posso usarlo anche con le variabili
x = 10
if x > 5:
    print("condizione vera!")
# l'indentazione è importante perchè è ciò che definisce cosa viene eseguito all'interno dello script
if True:
    print("sono nell\'if")
print("sono al di fuori dell\'if")


# operatore di comparazione
# sono 6:
# == #differisce dal singolo uguale, in quanto il singolo uguale assegna un valore, quello utile alle comparazioni è il doppio uguale; verifica che una variabile o un valore sia uguale ad un altro (es. if a == b)
# != #diverso, verifica che il a sia diverso da b (if a != b)
# >= #a maggiore uguale a b (if a >= b)
# <= #a minore uguale a b (if a <= b)
# >  #maggiore
# <  #minore
# N.B. in python possiamo anche effettuare comparazioni di verifica se una variabile o un valore è compreso tra due variabili o valori
# if 10 < x < 15:

# elif ed else
# se dovessi stampare un messaggio diverso a seconda se un valore è positivo o negativo dovremmo fare:
x = 5
y = 6
if x == y:
    print("i due valori sono uguali")
if x != y:
    print("i due valori sono diversi")

# fortunatamente però esistono due costrutti, elif ed else che ci permettono di inserire all'interno di un unico if i diversi risultati a seconda se la condizione sia verificata o meno
# else
# nel momento in cui la condizione non è veficata per un qualsiasi motivo, eseguo il secondo script
if x == y:
    print("i due valori sono uguali")
else:
    print("i due valori sono diversi")

#elif
# sta per "else if" e viene utilizzato per verificare una seconda condizione nel caso la prima non sia verificata
if x == y:
    print("i due valori sono uguali")
elif x > y:
    print("x è maggiore di y")
else:
    print("x è minore di y")

# di if e di else possono essercene solo 1, mentre possiamo inserire quanti elif desideriamo


#operatori logici and e or
# and #ci permette di verificare che una o più condizioni siano verificate contemporaneamente
x = -5
y = 10
if x != 0 and y != 0:
    print("entrambe le variabili sono diverse da 0")
# or  #ci permette di verificare che almeno una delle condizioni stabilite sia verificata
x = -5
y = 10
if x > 0 or y > 0:
    print("almeno una delle due variabili è maggiore di 0")

#esiste anche l'operatore not()
# questo operatore ci permette di "ragionare al contrario", chiediamo che la condizione che abbiamo inserito non sia verificata, e questo ci permetterà di entrare nella condizione vera dell'if
x = 2
if not(x != 2):
    print("""
          la condizione era: 
          x è diverso da 2? in questo caso la condizione sarebbe stata falsa
          essendo però presente il not prima della condizione
          la nostra condizione estesa sarebbe:
          verifica che non sia vero che x sia diverso da 2
          quindi la condizione è vera, in quanto è vero che non è vero che x sia diverso da due
          """)
    
#versione short hand
# può essere utilizzata solo nel caso in cui sia presente un unico statement dopo l'if
x = 5
if x > 0: print("x è maggiore di 0")
else: print("x è minore o uguale a 0")
# oppure
print("x è maggiore di 0") if x > 0 else print("x è minore o uguale a 0")

#if innestati
# mi permette di verificare una condizione successiva alla codnizione verificare
# ad esempio vado a verificare se x è maggiore di 0 solamente se è un numero pari
# n.b. per verificare se un numero è pari posso usare il modulo 2, se restituisce 0 è pari, altrimenti sarà dispari
x = 6
if x % 2 == 0:
    print("x è pari")
    if x > 0:
        print("x è pari, e maggiore di 0")
    else:
        print("x è pari, ma minore o uguale a 0")
else:
    print("x è dispari")