# cosa sono le funzioni?
# come si crea una funzione
# chiamare una funzione
# parametri di una funzione
# differenza tra argomenti e parametri
# arbitrary arguments, keyword arguments, arbitrary keyword arguments
# parametri di default
# return dei valori

# le funzioni, di base, sono un blocco di codice riutilizzabile, all'interno del quale ci sono delle istruzioni che verranno eseguite ogni volta che la funzione viene richiamata

# come si crea una funzione
def mia_funzione():
    print("esempio esecuzione 1")
    print("esempio esecuzione 2")
    print("esempio esecuzione 3")

# come chiamo la funzione?
mia_funzione()

# i parametri ci permetteranno di prendere degli argomenti
# i parametri vengono indicati in fase di definizione della funzione e si indicano tra parentesi
# gli argomenti invece dovranno essere inseriti in fase di chiamata della funzione
def mia_funzione(mio_parametro):
    print("esempio esecuzione" + mio_parametro)

mia_funzione("mio_argomento")

# arbitrary arguments, keyword arguments, arbitrary keyword arguments
# gli arbitrary arguments vengono gestiti quando non sappiamo la quantità di parametri che potrebbero essere utilizzati
# vengono gestiti inserendo l'asterisco prima del parametro in fase di esecuzione e indicando nella funzione gli indici in cui andranno inseriti gli argomenti specificata in fase di chiamata della funzione
def mia_funzione(*miei_parametri):
    print("esempio esecuzione " + miei_parametri[0])
    print("esempio esecuzione funzione secondo parametro " + miei_parametri[1])

mia_funzione("mio_argomento", "mio_argomento_2")    #il mio_argomento_2 è in indice 1

# keyword arguments
# sono argomenti che anzichè avere un indice, usano una chiave (che è il nome del parametro)
def mia_funzione(mio_param_1, mio_param_2):
    print("esempio esecuzione " + mio_param_1)
    print("esempio esecuzione funzione secondo parametro " + mio_param_2)

mia_funzione(mio_param_1 = "mio_argomento", mio_param_2 = "mio_argomento_2")


# parametri di default
# lo dice il nome stesso, identifico un argomento di default all'interno dei parametri
# nel momento in cui chiamerò la funzione senza specificare gli argomenti, verrà preso quello di default
def mia_funzione(mio_parametro = "questo è il mio parametro di default"):
    print("esempio esecuzione " + mio_parametro)

mia_funzione()


# return dei valori
# il return è fondamentale specificare cosa deve essere fornito come outoput della funzione
def esegui_somma(n_1, n_2):
    sum = n_1 + n_2
    return sum  #eseguendo il commento di questa riga di codice, non otterremo nessun outoput per x

x = esegui_somma(5, 7)

print(x)