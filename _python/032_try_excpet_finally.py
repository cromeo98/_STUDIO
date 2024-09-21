# definizione try, except, finally
# errore vs/exception handling
# multiple Exception
# else
# finally
# raise/throw exception
# a cosa servono?
# ad impedire che nel momento in cui il nostro programma riceve un errore, il nostro programma vada in crash
# try ci permette di testare un blocco di codice
# except ci permette di raccogliere l'errore testato
# finally ci permette di eseguire un ulteriore script una volta intercettato un errore
# come funziona?
# nel momento in cui incontriamo un errore (esempio provo a stampare la variabile x che non ho mai dichiarato) testando all'interno di un try gestiamo l'except, che conterrà lo script da eseguire in caso di errore (exception handling)
# anche se non dovessimo gestire nessuno script da eseguire in caso di errore (pass), il programma andrà avanti
# nel seguente esempio, dopo che il nostro primo print va in errore, non verrà eseguito più nulla (non verrà stampato "ciao" - NameError: name 'x' is not defined)
# print(x)
# print('ciao')
# lo stesso errore però, se gestito all'interno di try & excpet, non comporterà il blocco del programma
try:
    print(x)
except:
    #(print("trovato un errore"))
    pass
print("ciao")
# nell'excpet, possiamo specificare quale errore deve essere gestito; ad esempio nel seguente caso andiamo a gestire solamente l'errore NameError, pertanto se venisse intercettato un errore diverso, questo comporterà l'interruzione del programma (sulla documentazione è possibile trovare la lista degli errori)
# try:
#     print(x)
# except TabError:
#     #(print("trovato un errore"))
#     pass
# print("ciao")
# ho la possibilità di combinare più exception 
# try:
#     print(x)
# except NameError:
#     (print("errore Name error"))
# except:
#     (print("altro errore"))
# print("ciao")

# else, come nelle "normali" condizioni, ci permette di definire uno script da eseguire nel caso in cui non venga intercettato nessun errore nell'esecuzione del try
# try:
#     print("ciao")
# except:
#     print("ho trovato un errore")
# else:
#     print("non ho trovato alcun errore")

# finally invece viene eseguito indipendentemente dal risultato del try (sia che ci sia o che non ci sia un errore)
# try:
#     print("ciao")
# except:
#     print("ho trovato un errore")
# else:
#     print("non ho trovato alcun errore")
# finally:
#     print("c'è anche il finally!!")

# raise and throw un exception/come si lancia un Exception?
# nel caso in cui volessimo stoppare l'intero programma al verificarsi di una determinata condizione, possiamo lanciare un errore da noi definito
# in questo esempio, interrompiamo il programma se x è minore di 0
x = -1
if x < 0:
    raise Exception("X è minore di 0!! Interrompo il programma")

print("Questo ciao non verrà mai eseguito se x è minore di 0")