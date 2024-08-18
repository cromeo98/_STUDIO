# lo scope delle variabili è "l'area" dentro la quale sono valide le variabili
# ad esempio, una variabile dichiarata solamente all'interno di una funzione, sarà valida solamente all'interno della funzione
# es. definisco la variabile x all'interno della funzione, provando a stampare x al di fuori della funzione, questa non sarà definita
# questo scope si dice "locale", e si applica anche all'interno delle funzioni innestate

def funct():
    x = 400
    return x
#print(funct())  #stampo a schermo il return della funzione
#print(x)       #NameError: name 'x' is not defined

# lo scope globale invece è l'esatto contrario, ovvero ho una variabile che è valida ovunque e può essere ripresa all'interno di una funzione 
# n.b. per modificare una variabile globale all'interno di una funzione, devo anteporre global davanti alla variabile
x = 400
print(x)

def multiply_2():
    global x
    x *= 2
    return x

print(multiply_2())
print(x)